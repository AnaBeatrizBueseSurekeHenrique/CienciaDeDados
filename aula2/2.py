import numpy as np
array = np.arange(10)
print(array)
print('---------')
false = np.full(shape=(3,3),fill_value=True)
print(false)
print('-------')
#matriz falsa


print(array[array % 2 == 1])
print('---------')
array[array % 2 == 1] = -1
print(array)
print("----------")
array = np.random.randint(1, 100, size=(5,5))
print(array)
print(array.sum(axis=0))
print('---------')
print(array.max(axis=1))
print('----------')
a = np.array([1,2,3,4,5])
a += 2
print(a)

print('---------')

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.concatenate((a,b))
print(c)
print('------------')
array1d = np.array([10,20,30,40])
print(np.flip(array1d))

