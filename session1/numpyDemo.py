#!/usr/bin/enf python3
import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
print(type(A))
      
B = np.array([[5,6],[7,8]])
C = np.array([[2,3],[4,5]])

print ("\nA+B:")
print(A+B)

print("\nA*B:")
print(np.matmul(A,B))

print("\nTranspose Matrix A:")
print(A.transpose())

try:
    AInverted = np.linalg.inv(A)
except numpy.linalg.LinAlgError:
    print("Matrix cannot be inverted")
    # Not invertible. Skip this one.
    pass
else:
    print("\nInverted Matrix")
    print(AInverted)
    
    print ("\nTesting if matrix inversion was correct: A*AInverted:")
    print(np.matmul(A,AInverted))
    print ("\nTesting if matrix inversion was correct: AInverted*A:")
    print(np.matmul(AInverted,A))