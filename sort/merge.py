def merge_sort_recursive(arr):
    
    if len(arr) <= 1:
        return arr
        
    medio = len(arr) // 2
    
    izquierda = arr[:medio]
    derecha = arr[medio:]
    
    izquierda = merge_sort_recursive(izquierda)
    derecha = merge_sort_recursive(derecha)
    
    return merge(izquierda, derecha)

def merge(izquierda, derecha):

    resultado = []  
    i = j = 0 
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    
    return resultado


arr1 = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort_recursive(arr1))