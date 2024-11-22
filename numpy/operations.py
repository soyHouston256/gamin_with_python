import numpy as np

lista = [1,2]

print(lista * 2)
arr =  np.arange(0,10)
arr2 = arr.copy()
print(arr)
print(arr * arr2)
print(arr +2)
print(1/arr)

matriz = np.reshape(arr,(2,5))
matriz2 =  matriz.copy()
print(matriz)
print(np.matmul(matriz,matriz2.T))
print(matriz2 @ matriz.T)
