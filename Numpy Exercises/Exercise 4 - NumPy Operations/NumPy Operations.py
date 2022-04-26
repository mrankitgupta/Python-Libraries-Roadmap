import numpy as np

# Joining Numpy Arrays
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print(np.vstack((n1,n2)))

n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print(np.hstack((n1,n2)))

n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print(np.column_stack((n1,n2)))

# Numpy Intersection & Difference

# Intersection1D
n1 = np.array([10,20,30,40,50])
n2 = np.array([40,50,60,70,80])
print(np.intersect1d (n1,n2))

# Setdiff1d
print(np.setdiff1d (n1,n2))

print(np.setdiff1d (n2,n1))