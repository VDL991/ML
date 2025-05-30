import numpy as np
A = np.array([1,2,3])
B = np.array([[4,5,6],[7,8,9]])
c = np.vstack([A,B]) #vertically stack the arrays
print("vertically stack the arrays", "\n", c)
x = np.array([[1],[2]])
y = np.array([[9,8,7],[6,5,4]])
d = np.hstack([x,y]) #horizantlly stack the arrays
print("horizantlly stack the arrays", "\n", d)