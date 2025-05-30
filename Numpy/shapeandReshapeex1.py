#You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.
#Input Format
#A single line of input containing  space separated integers.
#Output Format
#Print the X NumPy array.
#Sample Input
#1 2 3 4 5 6 7 8 9
#Sample Output
#[[1 2 3]
 #[4 5 6]
 #[7 8 9]]
import numpy as np 
arr = input().strip().split()
arr = np.array(arr, dtype=int)
print(arr)
print(arr.shape)
r = arr.reshape(3,3)
print(r)

