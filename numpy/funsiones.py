import numpy as np

vector = np.random.randint(1,20,10)
print(vector)
matriz = np.reshape(vector,(2,5))
print(matriz)
print("max")
print(matriz.max(0))
print(matriz.max(1))

print(matriz.argmax(0))
print(matriz.argmax(1))


print(vector)
print(vector.ptp())
print(matriz)
print(matriz.ptp())

print("Columnas")
print(matriz.ptp(0))

print("Filas")
print(matriz.ptp(1))

print("Percentile") 
print(np.percentile(matriz,50))

print("Median") 
print(np.median(matriz))
print(np.std(matriz))
print(np.var(matriz))
#desviacion estandar al cuadraro sera igual que la varianza
print(np.std(matriz)**2)

#media suma de todos los valores entre la cantidad de items existentes
print(np.mean(matriz))

#Redimensionando
print("Redimensionando")
a = np.array([[1,2],[3,4]])
b = np.array([5,6])

b = np.expand_dims(b, axis=0)
c = np.concatenate((a,b),axis=0) 
print(c)

d = np.concatenate((a,b.T),axis=1) 
print(d)

