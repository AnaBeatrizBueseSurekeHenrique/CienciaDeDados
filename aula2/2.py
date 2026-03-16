import numpy as np
print("Criação array: ")
array = np.arange(10)
print(array)
print('---------')
print("Array Boleano: ")
false = np.full(shape=(3,3),fill_value=True)
print(false)
print('-------')
print('Extrair Impares')
print(array[array % 2 == 1])

print('---------')
print("Substituir valores")
array[array % 2 == 1] = -1
print(array)

print("----------")
print('Matriz aleatória')
array = np.random.randint(1, 100, size=(5,5))
print(array)

print('----------')
print('Soma por coluna')
print(array.sum(axis=0))

print('---------')
print("Máximo por linha")
print(array.max(axis=1))

print('----------')
print('Broadcasting simples')
a = np.array([1,2,3,4,5])
a += 2
print(a)

print('---------')
print("Concatenação")
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b))
print(c)

print('------------')
print('Inverter Array')
array1d = np.array([10,20,30,40])
print(np.flip(array1d))

