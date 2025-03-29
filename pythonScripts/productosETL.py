import pandas as pd
import gdown

# File URL (Google Drive)
productos_url = f'https://drive.google.com/uc?id=1ZaNq9OGOxvmzZbbDtp7ySXcSKj7Jq_4J'

# Download the file
gdown.download(productos_url, 'productos.csv', quiet=False)

# Read the raw CSV file with pandas
productos_data = pd.read_csv('productos.csv')

# Remove fields with NA (empty)
productos_data.dropna(inplace=True)

# Remove duplicates
productos_data.drop_duplicates(inplace=True)

# Remove products with IDs with decimal part
productos_data = productos_data[productos_data['producto_id'] % 1 == 0]

# Convert producto_id to type int
productos_data['producto_id'] = productos_data['producto_id'].astype('int')

# export modified dataframe to csv
productos_data.to_csv('productos_cleaned.csv', index=False)
