import pandas as pd
import gdown

# File URL (Google Drive)
ventas_url = f'https://drive.google.com/uc?id=1vpzNARlM0zdrPKlbbWKjuFawiLDvuw45'

# Download the file
gdown.download(ventas_url, 'ventas.csv', quiet=False)

# Read the raw CSV file with pandas
ventas_data = pd.read_csv('ventas.csv')

# Remove fields with NA (empty)
ventas_data.dropna(inplace=True)

# Remove duplicates
ventas_data.drop_duplicates(inplace=True)

# Remove products with IDs with decimal part
ventas_data = ventas_data[ventas_data['venta_id'] % 1 == 0]

# Convert venta_id to type int
ventas_data['venta_id'] = ventas_data['venta_id'].astype('int')

# Remove producto_id with decimal part
ventas_data = ventas_data[ventas_data['producto_id'] % 1 == 0]

# Convert producto_id to type int
ventas_data['producto_id'] = ventas_data['producto_id'].astype('int')

# Remove cliente_id with decimal part
ventas_data = ventas_data[ventas_data['cliente_id'] % 1 == 0]

# Convert cliente_id to type int
ventas_data['cliente_id'] = ventas_data['cliente_id'].astype('int')

# Remove sucursal_id with decimal part
ventas_data = ventas_data[ventas_data['sucursal_id'] % 1 == 0]

# Convert sucursal_id to type int
ventas_data['sucursal_id'] = ventas_data['sucursal_id'].astype('int')

# Convert cantidad to type int
ventas_data['cantidad'] = ventas_data['cantidad'].astype('int')

# export modified dataframe to csv
ventas_data.to_csv('ventas_cleaned.csv', index=False)