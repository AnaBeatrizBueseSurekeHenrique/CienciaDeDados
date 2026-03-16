import pandas as pd

df = pd.read_csv(
    'vendas.csv',
    sep=',',
    encoding='utf-8',
    parse_dates=['datetime', 'date'],
    index_col='datetime',
    usecols=['date', 'cash_type', 'money', 'coffee_name', 'datetime'],
    dtype={
        'money':'float64',
    },
    na_values=['-', 'NA']
)

print(df.info())
