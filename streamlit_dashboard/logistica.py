import streamlit as st
import matplotlib.pyplot as plt

# Main page content
st.markdown("# Logística 🗓️")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

enviosPorMes = """
SELECT
	EXTRACT(MONTH FROM fecha_envio) AS month,
	COUNT(*) AS shipments
FROM
	logistica
GROUP BY
	EXTRACT(MONTH FROM fecha_envio)
ORDER BY
	month;
"""

df1 = conn.query(enviosPorMes)

df1.rename(columns={'month': 'Mes', 'shipments': 'Envios'}, inplace=True)

st.title("Envíos por mes")

if st.checkbox('Mostrar envíos por mes'):
    st.dataframe(df1, hide_index=True)

st.line_chart(data=df1, x='Mes', y='Envios', x_label='Mes', y_label='Envíos', color='#FFA500', use_container_width=True)

enviosPorProveedor = """
SELECT
	logistica.proveedor_id,
	proveedores.nombre_proveedor,
	COUNT(*) AS shipments
FROM
	logistica
INNER JOIN proveedores ON logistica.proveedor_id = proveedores.proveedor_id
GROUP BY
	logistica.proveedor_id,
	proveedores.nombre_proveedor
ORDER BY
	shipments DESC
LIMIT 10;
"""

df2 = conn.query(enviosPorProveedor)

st.title("10 proveedores con más envíos")

df2.rename(columns={'proveedor_id': 'ID Proveedor', 'nombre_proveedor': 'Proveedor', 'shipments': 'Envios'}, inplace=True)

if st.checkbox('Mostrar envíos por proveedor'):
    st.dataframe(df2, hide_index=True)

st.bar_chart(df2, x="Proveedor", y="Envios", x_label="Proveedor", y_label="Número de envíos",
                 color="#FFA500")

enviosPorEstado = """
SELECT
	estado_envio,
	COUNT(*) AS envios
FROM
	logistica
GROUP BY
	estado_envio
ORDER BY
	envios DESC;
"""
df3 = conn.query(enviosPorEstado)

st.title("Envios por estado")

if st.checkbox('Mostrar envios por estado'):
    st.dataframe(df3, hide_index=True)

# Prepare data for the pie chart
estados = df3['estado_envio']
envios = df3['envios']

# Create the pie chart
fig, ax = plt.subplots()
ax.pie(envios, labels=estados, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Title
ax.set_title('Distribución de envios por estado')

# Display pie chart in Streamlit
st.pyplot(fig)