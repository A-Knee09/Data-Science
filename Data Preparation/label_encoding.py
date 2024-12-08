import pandas as pd

data = {
    'Product' : ['Laptop' , 'Tablet' , 'Smartphone']
}

df = pd.DataFrame(data)

label_mapping = {
    
    'Laptop' : 0,
    'Tablet' : 1,
    'Smartphone' : 2
}

df['Product_Code'] = df['Product'].map(label_mapping)
print(df)