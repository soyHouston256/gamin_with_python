def insertion_sort(array):
    for i in range(1, len(array)):
        current = array[i]
        j = i - 1
        while j>=0 and array[j] < current:
            array[j+ 1] = array[j]
            j -= 1
        array[j+1] = current
    return array
arr = [64, 34, 25, 12, 22, 11, 90]

print('Original',arr)

print('Ordenada', insertion_sort(arr))
