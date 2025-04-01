import streamlit as st

# Main page content
st.markdown("# Ventas 💲")

# Initialize connection.
conn = st.connection("postgresql", type="sql")

numVentas  = """
SELECT 
    sucursal_id,
    COUNT(sucursal_id) AS num_ventas
FROM 
    ventas
GROUP BY 
    sucursal_id
ORDER BY num_ventas DESC
LIMIT 10;"""

df1 = conn.query(numVentas)

st.title("10 sucursales con mayor número de transacciones")
if st.checkbox('Mostrar gráfica transacciones'):
    st.bar_chart(df1, x="sucursal_id", y="num_ventas", x_label="Sucursal", y_label="Número de transacciones",
                 color="#0096FF")

df1.rename(columns={'sucursal_id': 'ID Sucursal', 'num_ventas': 'Transacciones'}, inplace=True)
st.dataframe(df1, hide_index=True)


totalVentas = """
SELECT
    sucursal_id,
    SUM(total) AS total_ventas
FROM
    ventas
GROUP BY
    sucursal_id
ORDER BY total_ventas DESC
LIMIT 10;"""

df2 = conn.query(totalVentas)

st.title("10 sucursales con mayor total en ventas")
if st.checkbox('Mostrar grafica total en ventas'):
    st.bar_chart(df2, x="sucursal_id", y="total_ventas", x_label="Sucursal", y_label="Total en ventas", color="#85BB65")

st.data_editor(
    df2,
    column_config={
        'sucursal_id': st.column_config.Column('ID Sucursal'),
        'total_ventas': st.column_config.NumberColumn('Total en ventas', format="dollar")
    },
    hide_index=True
)

masVendidos = """
SELECT 
	ventas.producto_id,
	productos.nombre_producto,
	SUM(cantidad) as total_vendidos
FROM
	ventas
INNER JOIN productos ON ventas.producto_id = productos.producto_id
GROUP BY ventas.producto_id, productos.nombre_producto
ORDER BY total_vendidos DESC
LIMIT 10;"""

df3 = conn.query(masVendidos)
st.title("10 productos más vendidos")

df3.rename(columns={'producto_id': 'ID Producto', 'nombre_producto': 'Producto', 'total_vendidos' : "Total Vendidos"}, inplace=True)
st.dataframe(df3, hide_index=True)

ventasPorMes = """
SELECT
	EXTRACT(MONTH FROM fecha) AS month,
	SUM(total) AS total_sales
FROM
	ventas
GROUP BY
	EXTRACT(MONTH FROM fecha)
ORDER BY
	month;
"""

df4 = conn.query(ventasPorMes)

df4.rename(columns={'month': 'Mes', 'total_sales': 'Total Ventas'}, inplace=True)

st.title("Ventas por mes")

if st.checkbox('Mostrar ventas por mes'):
    st.data_editor(
        df4,
        column_config={
            'Total Ventas': st.column_config.NumberColumn(format="dollar")
        },
        hide_index=True
    )

st.line_chart(data=df4, x='Mes', y='Total Ventas', x_label='Mes', y_label='Total Ventas', color='#85BB65', use_container_width=True)