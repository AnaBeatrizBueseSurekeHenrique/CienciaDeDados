from collections import Counter
from bs4 import BeautifulSoup
import requests
from github import Github
from github import Auth
#exercicio 1: contagem de palavras
f = open("texto.txt")
words = f.read().split()
freq = Counter(words)
print("Exercicio 1")
for w, c in freq.items():
    print(w, ":", c)
f.close() 
print('----------')
print("Exercicio 2")
#exercicio 2: webcrapping simples
url = ("https://cursos.alura.com.br/forum/topico-sugestao-mudancas-na-api-do-twitter-286892")

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
# print(soup)
importantParagraphs  = soup('h2')
print(importantParagraphs)
print('--------')
#exercicio 3: Consumo de API (GitHub)
print('Exercicio 3')
auth = Auth.Token()
g = Github(auth=auth)
palavra = "data"

try:
    repos = g.search_repositories(palavra)
    for i in range(0,5):        
        print(f"Nome: {repos[i].name}")
        print(f"URL: {repos[i].html_url}")
        print(f"Descrição: {repos[i].description}")
        print('----------')
except Exception as e:
    print(f"Error finding repository: {e}")
g.close()
