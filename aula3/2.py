import pandas as pd

df = pd.read_csv(
    'clima.csv',
    encoding='utf-8',
    parse_dates=['Date'],
    index_col='Date',
    usecols=['Date','MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustDir','WindGustSpeed','WindDir9am','WindDir3pm','WindSpeed9am','WindSpeed3pm','Humidity9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm','RainToday','RainTomorrow'],
    na_values=['-', 'NA']
)

print(df.info())
