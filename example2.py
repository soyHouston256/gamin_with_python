import numpy as np

A = np.random.randint(1, 11, size=(4, 4)) 
B = np.random.randint(1, 11, size=(4, 4)) 
print("matriz A")
print(A)
print("matriz B")
print(B)
print("matriz A X B Dot")
print(np.dot(A,B))
print("matriz A X B matMul")
print(np.matmul(A, B))

det = np.linalg.det(A)
print(det)
while det < 0:
    A = np.random.randint(1, 11, size=(4, 4))
    det = np.linalg.det(A)
while det < 0:
    B = np.random.randint(1, 11, size=(4, 4))
    det = np.linalg.det(B)

print("matriz det(A) ")
print(np.linalg.det(A))

print("matriz det(B) ")
print(np.linalg.det(B))

print("matriz Inv(A) ")
print(np.linalg.inv(A))

print("matriz Inv(B) ")
print(np.linalg.inv(B))

print("matriz eig Values(A) ")
print(np.linalg.eig(A))
print("matriz eig Values(B) ")
print(np.linalg.eig(B))

print("matriz eig eigvals(A) ")
eigenvalores_A = np.linalg.eigvals(A)
print(eigenvalores_A)

print("matriz eig eigvals(B) ")
eigenvalores_B = np.linalg.eigvals(B)
print(eigenvalores_B)

concatenado  = np.concatenate((A,B), axis=1)
print(concatenado)

eigenvalores_apilados = np.concatenate((eigenvalores_A, eigenvalores_B))
eigenvalores_finales = np.sort(eigenvalores_apilados)
print(eigenvalores_apilados)
print("\nForma del array de eigenvalores:", eigenvalores_apilados.shape)

print("\n3. Eigenvalores ordenados:")
print(eigenvalores_finales)
print("Longitud:", len(eigenvalores_finales))