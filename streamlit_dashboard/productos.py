import streamlit as st
import matplotlib.pyplot as plt

st.markdown("# Productos 📦")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

df = conn.query('SELECT categoria, COUNT(*) AS cat_count FROM productos GROUP BY categoria ORDER BY cat_count DESC;')

cheap = conn.query('SELECT * FROM productos WHERE precio_base = (SELECT MIN(precio_base) FROM Productos);')
expensive = conn.query('SELECT * FROM productos WHERE precio_base = (SELECT MAX(precio_base) FROM Productos);')

st.title('Producto más barato')
st.dataframe(cheap, hide_index=True)

st.title('Producto más caro')
st.dataframe(expensive, hide_index=True)

st.title('Productos por categoría')
# Display the data in Streamlit
if st.checkbox('Mostrar dataframe 1'):
    st.dataframe(df, hide_index=True)

# Prepare data for the pie chart
categories = df['categoria']
product_counts = df['cat_count']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(product_counts, labels=categories, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
ax.set_title('Distribución de productos por categoría')

# Display pie chart in Streamlit
st.pyplot(fig)




