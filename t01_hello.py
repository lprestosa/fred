import pandas as pd
import fredapi
import configparser
import os

config = configparser.ConfigParser()
config.read('conf/config.ini')

# Replace API_KEY with your own FRED API key
api_key = config.get('API', 'key')
path = config.get('PATH', 'data_path')
os.makedirs(path, exist_ok=True)


# Create a FRED API object
fred = fredapi.Fred(api_key=api_key)

# Define the data series you want to download
series_id = 'GDPC1'  # Real Gross Domestic Product (GDP) in chained 2012 dollars

# Download the data using the FRED API
data = fred.get_series(series_id)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data, columns=['Value'])
csv_file = f"{path}/gross_domestic_product.csv"
df.to_csv(csv_file)

# Print the first 5 rows of the DataFrame
print(df)
