import numpy as np 
# m = ([78,67,56],[76,75,47],[84,59,60],[67,72,54])
# Marks = np.array(m)
# print(Marks[0:4,2])
# A = np.arange(1,15)
# print(A[3:6])

# #retrieving inner 3*3 matrix

# B = np.random.randint(1,100,(5,5))
# print(B)
# print(B[1:4,1:4])

##Row wise reverse 
c = np.random.randint(1,100,(4,3))
print(c)
#print("After Row wise reverse")
#print(c[::-1,:])

##column wise reverse
#print("After column wise reverse") 
#print(c[:, ::-1])

# At a time both row wise and col wise reverse
print("At a time both row wise and col wise reverse") 
print(c[::-1,::-1])