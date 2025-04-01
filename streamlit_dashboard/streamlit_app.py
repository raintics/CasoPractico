import streamlit as st

# Define the pages
main_page = st.Page("clientes.py", title="Clientes", icon="👤")
page_2 = st.Page("productos.py", title="Productos", icon="📦")
page_3 = st.Page("proveedores.py", title="Proveedores", icon = "🚚")
page_4 = st.Page("ventas.py", title="Ventas", icon = "💲")
page_5 = st.Page("logistica.py", title="Logística", icon = "🗓️")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()