import pandas as pd

data = {
    
    'Name' : ['Ani' , 'Ana' , 'Mark','Daniel' , 'run'],  # run -> Ron   
    'Age' : [21, 22, 32, 19, 27]
}
df = pd.DataFrame(data)

df['Index'] = range(1,len(df)+1)
print(df)

df['Name'] = df['Name'].replace({'run' : 'Ron'})
print(df)

