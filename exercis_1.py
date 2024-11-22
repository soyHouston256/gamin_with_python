import numpy as np

random_ints = np.random.randint(-50, 51, (10, 10)) 

#mask = random_ints > 0
print("Original: ")
print(random_ints)
print("")
random_ints[random_ints<0] = 0 
print("Ceros: ")
print(random_ints)


scale = random_ints / random_ints.max()
print("Método 1 - División por el máximo:")
print(scale)
rs = scale.reshape((5, 20))
print(rs)

third = rs[:,2]

print("Tercera", third)

print(third.mean())
print(np.median(third))
print(third.std())
print(third.std()**2)
print(third.var())

#array total
print("Hallando datos del total")
percentile = np.percentile(rs,90)
median = np.mean(rs)
print(percentile)
mask = rs > percentile
rs[mask] = median
print(rs)

print(np.sort(rs, axis=1))

plano = rs.flatten()

print(plano)
# 3. Obtener elementos únicos ordenados
elementos_unicos = np.unique(plano)
print("\nElementos únicos ordenados:", elementos_unicos)
