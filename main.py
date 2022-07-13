import pandas as pd

data = pd.read_csv('products_data.csv')

print(data['Product_attributes'][0])

