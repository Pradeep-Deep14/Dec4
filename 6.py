import numpy as np

def add_arrays(arr1,arr2):
    return np.add(arr1,arr2)

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

result= add_arrays(arr1,arr2)
print(result)