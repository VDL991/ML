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
rows = int(input("Enter row number only"))
columns = int(input("Enter column number only"))
print(arr)
print(arr.shape)
if len(arr)!= rows * columns:
    print(f"cannot reshape array of size {len(arr)} in to shape({rows},{columns})")
else:
 r = arr.reshape(rows,columns)
 print(r)

