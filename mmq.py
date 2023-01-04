import numpy as np
ar = np.array
def mmq(A,b):
    nA = np.dot( np.transpose(A), A)
    nb = np.dot( np.transpose(A), b)
    return np.linalg.solve(nA,nb)
    


# A = ar([[1, 1],[1, 2],[1, 3],[1, 4]])
# b = ar([[1.3],[3.5],[4.2],[5.0]])
# print(mmq(A,b))

# A = ar([[1, 1],[1, 2],[1, 3],[1, 4]])
# b = np.transpose(ar([]))
# print(mmq(A,b))

# k = (2/3*1/90*(np.pi*10)**5) **(1/4)
# print(k)

W = [400.0,216.6,134.5,115.4,97.1,77.9,67.0,57.7,56.0,52.1]
C = [[84.8,42.9,26.7,22.7,19.2,15.6,13.8,12.3,11.5,11.1]]

A = np.transpose(ar([
    [1 for i in range(len(W))] , 
    W
]))

b = np.transpose(ar(C))
print(A)
print(b)
print(mmq(A,b))
