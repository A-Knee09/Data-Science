import pandas as pd

data = {
    'city' : ['New york' , 'Los angeles' , 'Chicago' , 'New york' , 'Chicago']
}

df = pd.DataFrame(data)

df = pd.get_dummies(df , columns=['city'])

print(df)