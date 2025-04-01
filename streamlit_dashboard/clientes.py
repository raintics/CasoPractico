import streamlit as st
import matplotlib.pyplot as plt

# Main page content
st.markdown("# Clientes 👤")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

df1 = conn.query('SELECT ubicacion, COUNT(*) AS cant_clientes FROM clientes GROUP BY ubicacion ORDER BY cant_clientes DESC;')
df1['color'] = ['Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul']

st.title('Clientes por ciudad')

# Display the data in Streamlit
if st.checkbox('Mostrar dataframe 1'):
    st.dataframe(df1, hide_index=True)

df1['latitude'] = [32.5149, 19.0413, 19.4326, 25.6866, 20.6597]
df1['longitude']  = [-117.0382, -98.2063, -99.1332, -100.3161, -103.3496]
# Add a 'Size' column, scaled based on suppliers count
df1['Size'] = df1['cant_clientes'] * 10  # Adjust multiplier as needed
df1['color_codes'] = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF']

# Use Streamlit to show the map with sized dots
st.map(df1, latitude="latitude", longitude="longitude", size="Size", color="color_codes")

# Prepare data for the pie chart
cities = df1['ubicacion']
clients_counts = df1['cant_clientes']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(clients_counts, labels=cities, colors=df1['color_codes'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
ax.set_title('Distribución de clientes por ciudad')

# Display pie chart in Streamlit
if st.checkbox('Mostrar gráfica clientes/ciudad'):
    st.pyplot(fig)


df2 = conn.query('SELECT genero, COUNT(*) AS gen_count FROM clientes GROUP BY genero ORDER BY gen_count DESC;')

st.title('Clientes por género')
if st.checkbox('Mostrar dataframe 2'):
    st.dataframe(df2, hide_index=True)

genders = df2['genero']
clients_counts2 = df2['gen_count']

# Create the pie chart
fig2, ax2 = plt.subplots()
ax2.pie(clients_counts2, labels=genders, colors=['#FF13F0','#D3D3D3','#1F51FF'], autopct='%1.1f%%', startangle=90)
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
ax2.set_title('Distribución de clientes por genero')

# Display pie chart in Streamlit
st.pyplot(fig2)

