import pandas as pd
import gdown

# File URL (Google Drive)
clientes_url = f'https://drive.google.com/uc?id=11BrwyIN5cUv27yDwIFoOCzi-Ch5y7MyB'

# Download the file
gdown.download(clientes_url, 'clientes.csv', quiet=False)

# Read the raw CSV file with pandas
clientes_data = pd.read_csv('clientes.csv')

# Remove fields with NA (empty)
clientes_data.dropna(inplace=True)

# Remove duplicates
clientes_data.drop_duplicates(inplace=True)

# Remove age outliers
clientes_data = clientes_data[clientes_data['edad'] < 90]

# change age field to type int
clientes_data['edad'] = clientes_data['edad'].astype('int')

# Change id field to type int
clientes_data['cliente_id'] = clientes_data['cliente_id'].astype('int')

# export modified dataframe to csv
clientes_data.to_csv('clientes_cleaned.csv', index=False)
