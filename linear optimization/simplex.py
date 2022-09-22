import itertools
import numpy as np

def getcolumn(M,i):
    ret = np.array([])
    for linha in M:
        ret = np.append(ret,[linha[i]])
    return ret


class Solve:
    def __init__(self,A,b,c) -> None:
        # formato padrão
        self.A = np.array(A)
        self.b = np.array(b)
        self.c = np.array(c)
        self.n = len(c)
        self.m = len(b)
    def matrixBase(self, indices):
        B = np.array([])
        for i in range(len(self.A)):
            linha = []
            for j in range(len(self.A[0])):
                if j in indices:
                    linha.append(self.A[0,j])
            B = np.concatenate(M,linha,axis=0)
        return B
    def solveBase(self,B,indices):
        invB = np.linalg.inv(B)
        xb = iter(np.dot(invB,self.b))
        x = []
        for i in range(m):
            if x in indices:
                x.append(next(xb))
            else:
                x.append(0)
    def cost(self,x):
        return np.dot(np.transpose(self.c),x)
    def viable(self,x):
        for x_ in x: 
            if x_ < 0: 
                return False
        return True 
    
    def tryAll(self):
        pass  




