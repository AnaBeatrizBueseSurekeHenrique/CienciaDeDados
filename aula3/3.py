import pandas as pd

df = pd.read_csv(
    'weblog.csv',
    # sep=';',
    encoding='utf-8',
    parse_dates=['Time'],
    index_col='Time',
    usecols=['IP','Time','URL','Staus'],
    na_values=['-', 'NA'],
    engine='python',
    skiprows=2,
    nrows=2
)

print(df)
