import numpy as np
# concatenating x,y,z arrays and assigning it to A
# x = np.array([1,2,3])
# y = np.array([4,5,6])
# z = np.array([7,8,9])
# A = np.concatenate([x,y,z])
# print(A)

# Row wise concentation of B to A
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.zeros([3,3], dtype=int)
c = np.concatenate((A,B), axis = 1) #Row wise
d = np.concatenate((A,B), axis = 0) # column wise
print("Row wise concentation result"," \n ", c)
print("column wise concentation result", " \n ", d)


