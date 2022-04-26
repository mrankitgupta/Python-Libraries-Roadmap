import numpy as np

# Basics
n1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (n1)
print(n1[0])
print(n1[2])
print(n1[:,1])
print(n1[:,2])

# Transpose Matrix
print(n1.transpose())

# Matrix Multiplication
n2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(n2)
print(n1.dot(n2))
print(n2.dot(n1))

# numpy.matlib.empty()
import numpy.matlib
print (np.matlib.empty((2,2)))
# filled with random data

# numpy.matlib.eye()
import numpy.matlib
print (np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))