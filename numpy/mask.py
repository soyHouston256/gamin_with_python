import numpy as np

arr = np.linspace(1,10,10, dtype='int8')
print(arr)
print(arr>5)
mask =  arr > 5
mask_2 =  arr < 9


print(arr[mask & mask_2])
arr[mask & mask_2] = 99
print(arr) 