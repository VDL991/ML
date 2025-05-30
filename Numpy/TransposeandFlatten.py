import numpy as np
N = int(input("Enter rows:"))
M = int(input("Enter columns:"))
arr = list(map(int, input(("Enter array elements")).strip().split())) # Input the flat list of elements
arr1 = np.array(arr).reshape(N,M)  # Convert to 2D NumPy array
print("original array", arr1)
#arr2 = arr1.transpose()
#print(arr2)
#arr3 = arr1.flatten()
#print (arr3)

def trans(arr):
    arr2 = arr.transpose()
    return arr2
def flat(arr):
    arr3 = arr.flatten()
    return arr3
T = trans(arr1)
F = flat(arr1)
print("Transpose of a given array", T)
print("Flat of a given array", F)