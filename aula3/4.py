import pandas as pd

df = pd.read_csv(
    'sales_data.csv',
    encoding='utf-8',
    parse_dates=['Date'],
    index_col='Date',
    usecols=['Date','Store ID','Product ID','Category','Region','Inventory Level','Units Sold','Units Ordered','Price','Discount','Weather Condition','Promotion','Competitor Pricing','Seasonality','Epidemic','Demand'],
     dtype={
        'Price':'float64',
        'Competitor Pricing': 'float64'
    },
    na_values=['-', 'NA']
)

print(df.info())
