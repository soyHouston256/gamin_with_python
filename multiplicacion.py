def multiplicacion(A, B):
    row_a = len(A)
    col_a = len(A[0])
    col_b = len(B[0])
    C = [[0 for _ in range(row_a)] for _ in range(col_b)]
    for i in range(row_a):
        for j in range(col_b):
            for k in range(col_a):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1, 2], [3, 4]]
B = [[1, 2], [3, 4]]
result = multiplicacion(A, B)
print(result)


C =[[7, 4], [3, 8],[2, 5]]
D =[[1, 6, 3],[9, 4, 2]] 
result2=multiplicacion(C, D)
print(result2)
result3=multiplicacion(D, C)
print(result3)
def imprimir(matriz):
    for row in matriz:
        print(row)

imprimir(result3)
imprimir(result2)