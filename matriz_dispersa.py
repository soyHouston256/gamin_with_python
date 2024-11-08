matrix = [ 
    [0,0,0,1,0],
    [0,0,0,0,0],
    [0,2,0,0,0],
    [0,0,0,0,0],
    [0,0,0,3,0]] 
dictionary = {
    (0,3):1,
    (2,1):2,
    (4,3):3
}
n = 5
matriz = []
for row in range(n):
    fila = []
    for col in range(n):
        item = dictionary.get((row, col), 0)
        fila.append(item)
    matriz.append(fila)

for row in matriz:
    print(row)


