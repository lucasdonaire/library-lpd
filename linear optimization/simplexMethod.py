import itertools
import numpy as np
Tr = np.transpose

def Simplex(A,b,c):
    n = len(c)
    m = len(b)
    
    # initial solution

    A0 = np.concatenate((A,np.eye(m)),axis=1)
    c0 = np.concatenate((np.zeros(n),np.ones(m)),axis=0)
    bindArtificial = [n+i for i in range(m)]
    Binv = np.eye(m)
    T = InitialTableau(A0,b,c0,Binv,bindArtificial)
    print(T)
    T,bind,cost,x = iterateTableau(T,bindArtificial)
    if cost != 0: print('o problema é inviável') ; return
    for i in bindArtificial:
        if i in bind:
            print("fudeu")
    
    # remove artificial variables
    T = T[:,:n]

    # transform 0 line
    T[0] = np.concatenate((
            [-np.dot( np.array([c[i] for i in bind]),x)], 
            c - np.dot(np.array([c[i] for i in bind]),T[1:,1:])
            ),axis=0)

    # iterate again
    T, bind, cost, x = iterateTableau(T,bind)

    # see results
    if cost == -np.inf: print('o custo é -inf') ; return
    print(f'o custo é {cost} em x = {x}')

def InitialTableau(A,b,c,Binv,bind):
    BinvA = np.dot(Binv, A)
    Binvb = np.dot(Binv, b)
    cB = np.array([c[i] for i in bind])
    custo = np.dot(cB,Binvb)
    cbar = c - np.dot(cB,BinvA)
    l0 = np.concatenate(([-custo] , cbar),axis=0)
    li =  np.concatenate(( Tr([Binvb]) , BinvA ),axis= 1)
    return np.concatenate(([l0],li),axis = 0)



def iterateTableau(T, bind): # viable tableau
    m,n = T.shape[0]-1,T.shape[1]-1
    while any(T[0,1:] < 0): 
        print(T)
        # uma iteracao
        j = next(x for x in T[0,1:] if x < 0)
        xB = T[1:,0]
        u = T[1:,j]
        minimo = np.inf
        l = -1
        # for i in range(m):
        for i, valor in enumerate(xB/u): # funfa?
            if u[i] > 0:
                # xbu = -xB[i]/u[i]
                xbu = -valor
                if xbu < minimo:   
                    minimo = min(minimo, xbu)
                    l = i # de 0 ate m-1
                if xbu == minimo:
                    # ordem lexicografica
                    pass
        if l == -1:
            dB = -u 
            return T,bind,-np.inf,dB # custo otimo -inf
        
        bind[l] = j
        T = col2base(T,l,j)
        
                
                
    return T, bind, -T[0,0], T[1:,0] # custo finito





def col2base(M,lin,col):
    M = np.array(M,dtype=np.float64)
    pivo = M[lin,col]
    M[lin] = M[lin]/pivo
    for linha in range(len(M)):
        if linha != lin:
            M[linha] = M[linha] - M[linha,col]*M[lin]
    return M






def main():
    A = np.array([
        [1, 2, 3, 4],
        [1, 1, 1, -1]
    ])
    c = np.array([1, -1, 0, 3])
    b = np.array([4, 8])
    Simplex(A,b,c)
main()

