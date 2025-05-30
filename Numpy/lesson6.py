import numpy as np 
A =np.random.randint(10,50,[5,5])
print(A)
print(np.sum(A, axis =1)) #axis=1 → operates across columns (row-wise)
print(np.sum(A, axis= 0)) #	axis=0 → operates down rows (column-wise)