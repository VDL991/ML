import numpy as np 
l = ([78, 67, 56],[76,75,47],[84,59,60],[67,72,54],[12,22,33])
A = np.array(l)
print(A)
print("Splitting array using numpy split")
b,c,d = np.split(A,(1,4),axis=0)
print(b,c,d, sep="\n\n")