import numpy as np
def arrays(arr):
    # complete this function
    # use numpy.array
    
    # Convert to NumPy array with float type
    np1 = np.array(arr, dtype=float) 
    return np1[::-1]  # Reverse and return

# Read input from user
arr = input().strip().split(' ')  
print(arrays(arr))