import pandas as pd

df = pd.read_csv(
    'Sales Transaction v.4a.csv',
    encoding='utf-8',
    parse_dates=['Date'],
    usecols=['TransactionNo','Date','ProductNo','ProductName','Price','Quantity','CustomerNo','Country'],
     dtype={
        'Price':'float64',
    },
    na_values=['-', 'NA'],
    decimal='.'
)

print(df.info())
