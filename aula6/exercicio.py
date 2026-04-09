#1 leitura avançada
#2 manipu
#3 consumindo api 
# 4 conexão com banco de dados
import os
import sqlalchemy as sqla
import pytumblr
import json
import requests
print("Leitura avançada")

import pandas as pd
df = pd.read_csv(
    'aula6\student_exam_scores.csv',
    encoding='utf-8',
    # parse_dates=['StartTime(UTC)', 'EndTime(UTC)'],
    # index_col='EventId',
    # usecols=['EventId','Type','Severity','StartTime(UTC)','EndTime(UTC)','Precipitation(in)','TimeZone','AirportCode','LocationLat','LocationLng','City','County','State','ZipCode'],
    na_values=['ND'],
    header=None,
    index_col=0
)

print(df.info())
print(df)
print("Manipulação de Excel")
df.to_excel("aula6\\RelatorioAnual.xlsx", sheet_name="Resultados")
df2 = pd.read_excel("aula6\\Vrinda Store Data Analysis.xlsx", sheet_name="Dados Brutos")
print(df2)
#2
print("Consumindo APIs")

json_file_path = r"credenciais.json"
imagens = "tumblr_avatars"
posts = "posts_data.json"

if not os.path.exists(imagens):
  os.makedirs(imagens)

with open(json_file_path, "r") as f:
    credentials = json.load(f)
    client = pytumblr.TumblrRestClient(
      credentials["consumer_key"],
      credentials["consumer_secret"],
      credentials["oath_token"],
      credentials["oath_secret"]
    )
    dashboard_posts = client.dashboard()
    if 'posts' in dashboard_posts:
      posts_lista = dashboard_posts['posts']
      df = pd.DataFrame(posts_lista)
      print(df)
print("Conexão com Banco de Dados")
db = sqla.create_engine("sqlite:///exaula6.sqlite")
df = pd.read_sql("SELECT * FROM produtos", db)
print(df)

