import numpy as np

arr = np.arange(11)
print(arr)

trozo = arr[0:6]
print(trozo)

trozo[:] = 0

print(trozo)
print(arr)

arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
print(arr)