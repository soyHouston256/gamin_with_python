import matplotlib.pyplot as plt # type: ignore
import time

def mistery_sort(arr):
    i = 1
    while i < len(arr):
        plt.bar(range(len(arr)), arr)
        plt.title(f'Iteración {i}')
        plt.pause(0.5)  # Pausa para la visualización
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        else:
            i += 1
    
    plt.bar(range(len(arr)), arr)
    plt.title('Ordenamiento completo')
    plt.show()  # Mostrar el gráfico final

# Lista aleatoria
lista_random = [1, 2, 3, 4]
print("Lista original:", lista_random)
plt.figure(figsize=(8, 6))
mistery_sort(lista_random)