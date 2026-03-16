def estatisticas(*numeros):
    print(f"Menor = {min(numeros)}")
    print(f"Maior = {max(numeros)}")
    media = sum(numeros)/len(numeros)
    print(f"Media = {media: .2f}")
    
estatisticas(1,2,3,4,5)