import pandas as pd

df = pd.read_csv(
    'WeatherEvents.csv',
    encoding='utf-8',
    parse_dates=['StartTime(UTC)', 'EndTime(UTC)'],
    index_col='EventId',
    usecols=['EventId','Type','Severity','StartTime(UTC)','EndTime(UTC)','Precipitation(in)','TimeZone','AirportCode','LocationLat','LocationLng','City','County','State','ZipCode'],
    na_values=['-', 'NA']
)

#
print(df.info())