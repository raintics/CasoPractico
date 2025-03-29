import pandas as pd
import gdown

# File URL (Google Drive)
proveedores_url = f'https://drive.google.com/uc?id=1N7D5SexMIOp0mHfn90DqBnXxU061sCsV'

# Download the file
gdown.download(proveedores_url, 'proveedores.csv', quiet=False)

# Read the raw CSV file with pandas
proveedores_data = pd.read_csv('proveedores.csv')

# Remove fields with NA (empty)
proveedores_data.dropna(inplace=True)

# Remove duplicates
proveedores_data.drop_duplicates(inplace=True)

# Remove products with IDs with decimal part
proveedores_data = proveedores_data[proveedores_data['proveedor_id'] % 1 == 0]

# Change id field to type int
proveedores_data['proveedor_id'] = proveedores_data['proveedor_id'].astype('int')

# export modified dataframe to csv
proveedores_data.to_csv('proveedores_cleaned.csv', index=False)