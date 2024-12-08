import pandas as pd

from sklearn.preprocessing import StandardScaler

data = {
    'Name' : ['Mark' , 'Dan' , 'Ron'],
    'Salary' : [50000, 60000 , 70000]
}

df  = pd.DataFrame(data)

scaler = StandardScaler()

df['Salary_Standardize'] = scaler.fit_transform(df[['Salary']])
print(df)