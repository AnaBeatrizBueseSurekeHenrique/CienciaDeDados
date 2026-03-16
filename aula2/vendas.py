import numpy as np

array = np.random.randint(100, 500, size=(12))
array = array.reshape((3,4))
print("Vendas:    ")
print(array)
val = array.sum(axis=1)
print(f"Venda por semana: {val}")

val = array.mean(axis=0)
print(f"Media por semana: {val}")
print(f"Houve {len(array[array > 400])} dia(s) onde houve vendas maiores que 400")