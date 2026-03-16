import pandas as pd

df = pd.read_csv(
    'Orange Quality Data.csv',
    sep=',',
    encoding='utf-8',
    usecols=['Size (cm)','Weight (g)','Brix (Sweetness)','pH (Acidity)','Softness (1-5)','HarvestTime (days)','Ripeness (1-5)','Color','Variety','Blemishes (Y/N)','Quality (1-5)'],
    dtype={
        'Size (cm)':'float64',
        'Brix (Sweetness)': 'float64',
        'pH (Acidity)': 'float64',
        'Softness (1-5)': 'float64',
        'Quality (1-5)': 'float64'
    },
    na_values=['-', 'NA']
)

print(df.head())
print(df.tail())
print('----------------')
v = df.describe()
print(v)
print(v['Size (cm)'])
print('----------------')

print(v['Weight (g)'])
print('----------------')

print(v['Brix (Sweetness)'])
print('----------------')

print(v['pH (Acidity)'])
print('----------------')

print(v['Softness (1-5)'])
print('----------------')

print(v['HarvestTime (days)'])
print('----------------')

print(v['Ripeness (1-5)'])
print('----------------')

print(v['Quality (1-5)'])

