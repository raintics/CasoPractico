import pandas as pd
import gdown

# File URL (Google Drive)
logistica_url = f'https://drive.google.com/uc?id=1lFiCrPo1p4PfflBJ6YJvlAXUa_FCqMB-'

# Download the file
gdown.download(logistica_url, 'logistica.csv', quiet=False)

# Read the raw CSV file with pandas
logistica_data = pd.read_csv('logistica.csv')

# Remove fields with NA (empty)
logistica_data.dropna(inplace=True)

# Remove duplicates
logistica_data.drop_duplicates(inplace=True)

# Remove envio_id with decimal part
logistica_data = logistica_data[logistica_data['envio_id'] % 1 == 0]

# Convert envio_id to type int
logistica_data['envio_id'] = logistica_data['envio_id'].astype('int')

# Remove venta_id with decimal part
logistica_data = logistica_data[logistica_data['venta_id'] % 1 == 0]

# Convert venta_id to type int
logistica_data['venta_id'] = logistica_data['venta_id'].astype('int')

# Remove proveedor_id with decimal part
logistica_data = logistica_data[logistica_data['proveedor_id'] % 1 == 0]

# Convert proveedor_id to type int
logistica_data['proveedor_id'] = logistica_data['proveedor_id'].astype('int')

# export modified dataframe to csv
logistica_data.to_csv('logistica_cleaned.csv', index=False)
