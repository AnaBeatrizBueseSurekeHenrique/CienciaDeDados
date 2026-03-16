import pandas as pd

df = pd.read_csv(
    'Sales Transaction v.4a.csv',
    encoding='utf-8',
    parse_dates=['Date'],
    index_col='student_id',
    usecols=['student_id','hours_studied','sleep_hours','attendance_percent','previous_scores','exam_score'],
     dtype={
        'Price':'float64',
    },
    na_values=['-', 'NA'],
    decimal='.'
)

print(df.info())
