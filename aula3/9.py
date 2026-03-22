import pandas as pd

df = pd.read_csv(
    'Students_Grading_Dataset.csv',
    encoding='utf-8',
    index_col='Student_ID',
    usecols=['Student_ID','First_Name','Last_Name','Email','Gender','Age','Department','Attendance (%)','Participation_Score','Projects_Score','Total_Score','Grade','Study_Hours_per_Week','Extracurricular_Activities',
             'Internet_Access_at_Home','Parent_Education_Level','Family_Income_Level','Stress_Level (1-10)',
             'Sleep_Hours_per_Night','Sleep_Hours_per_Night_Entier','Country'],
     dtype={
        'Attendance (%)':'float64',
        'Participation_Score': 'float64',
        'Projects_Score': 'float64',
        'Total_Score': 'float64',
        'Study_Hours_per_Week': 'float64',
        'Sleep_Hours_per_Night': 'float64'
    },
    na_values=['-', 'NA'],
    decimal='.'
)

print(df.describe())
