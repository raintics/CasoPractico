import streamlit as st
import matplotlib.pyplot as plt

# Main page content
st.markdown("# Proveedores 🚚")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT ubicacion, COUNT(*) AS cant_prov FROM proveedores GROUP BY ubicacion ORDER BY cant_prov DESC;')
df['color'] = ['Rojo', 'Naranja', 'Amarillo', 'Verde', 'Azul']

st.title('Proveedores por ciudad')
# Display the data in Streamlit
if st.checkbox('Mostrar dataframe'):
    st.dataframe(df, hide_index=True)


df['latitude'] = [25.6866, 32.5149, 20.6597, 19.0413, 19.4326]
df['longitude']  = [-100.3161, -117.0382, -103.3496, -98.2063, -99.1332]
# Add a 'Size' column, scaled based on suppliers count
df['Size'] = df['cant_prov'] * 2000  # Adjust multiplier as needed
df['color'] = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF']

# Use Streamlit to show the map with sized dots
st.map(df, latitude="latitude", longitude="longitude", size="Size", color="color")


# Prepare data for the pie chart
cities = df['ubicacion']
prov_counts = df['cant_prov']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(prov_counts, labels=cities, colors=df['color'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
ax.set_title('Distribución de proveedores por ciudad')

# Display pie chart in Streamlit
if st.checkbox('Mostrar gráfica'):
    st.pyplot(fig)