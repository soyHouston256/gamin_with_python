import numpy as np

arr = np.array([1,2,3,4,5,5])

print(type(arr))

matrix = [[1,2,3],[4,5,6],[7,8,9]]

npm = np.array(matrix)

print(npm[1,1])

print(matrix[1][1])

print(matrix[0:3])
print(npm[1:,0:2])
vector = np.array([1,2,3,4,5,6,7,8,9])
print(vector[2:])
print(vector[::3])

array_1 = np.array([1,2,3,4])

print(arr.dtype)

array_2 = np.array([1,2,3,4,5,6], dtype='float64')

print(array_2)
print(array_2.dtype)

print(array_1.astype(np.float64))

#Dimensiones
##Escalar
##Vector
##Matriz
##Tensor

scalar = np.array(42)
print(scalar)

vector = np.array([1,2,3,4,5,6,7])
print(vector)

matriz = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print(matriz)
print(matriz.ndim)

tensor = matriz = np.array([[[1,2,3,],[4,5,6],[7,8,9]],[[1,2,3,],[4,5,6],[7,8,9]]])
print(tensor)
print(tensor.ndim)


#definir el numero dimensiones
vector_redin = np.array([1,2,3], ndmin=10)  
print(vector_redin)

#Eliminar dimensiones - Elimina los que no se estan usando
vector_expand = np.expand_dims(vector_redin, axis=0)
print(vector_expand.ndim)
vector_del = np.squeeze(vector_expand)
print(vector_del, vector_del.ndim)


array_range = np.arange(10)
print(array_range)


array_range_2 = np.arange(0,10,2)
print(array_range_2)

array_zeros = np.zeros(3)
print(array_zeros)


matrix_zeros = np.zeros((3,3))
print(matrix_zeros)


matrix_ones = np.ones((3,3))
print(matrix_ones)


matrix_lins = np.linspace(0,10,100)
print(matrix_lins)

#matriz indentidad de tamaño n
matrix_eye = np.eye(5)
print(matrix_eye)

print(np.random.rand(4,4))
print(np.random.randint(1,15))
print(np.random.randint(1,100,(10,10)))

array_shape = np.random.randint(1,50,(5,2))
print(array_shape)
print(array_shape.shape)

#print(array_shape.reshape(2,5))

print(np.reshape(array_shape,(2,5)))



