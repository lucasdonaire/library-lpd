import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# função para plotar resultados
def plotmult(listF, interval=[0,10]):
    x = np.linspace(interval[0], interval[1], 1000)
    for f in listF:
        y = list()
        for i in range(len(x)):
            y.append(f(x[i]))
        y = np.array(y)
        plt.plot(x, y) 
    plt.show()


def CompositeSimpsonRule(f,a,b,n=100):
    # n par
    # algoritmo 4.1
    h = (b-a)/n
    X0 = f(a) + f(b)
    X1 = 0
    X2 = 0
    for i in range(1,n):
        x = a+i*h
        if i % 2 == 0:
            X2 += f(x)
        else:
            X1 += f(x)
    return h*(X0+4*X1+2*X2)/3


def richardson(LN1):
    # recebe LN1 = [N1(h),N1(h/2),...,N1(h / 2^(n-1))]
    # onde f(h) = N1(h) + K1*h^2 +k2*h^4 + ... 
    # retorna tabela com a extrapolação de richardson
    n = len(LN1)
    M = np.zeros((n,n))
    for j in range(n):
        M[j,0] = LN1[j]
    
    for i in range(1,n):
        for j in range(i,n):
            res = M[j,i-1]+(M[j,i-1]-M[j-1,i-1])/(4**(i)-1)
            M[j,i] = res
    
    return M


def RombergAlgorithm(f,a,b,n=5):
    h = [(b-a)/2**(k-1) for k in range(1,n+1)]
    r = [h[0]*(f(a)+f(b))/2]
    for k in range(1,n):
        soma = 0
        for i in range(1,2**(k-1)+1):
            soma += f(a + (2*i-1)*h[k])
        r.append( (r[k-1] + h[k-1] * soma)/2 )
        # calcula aproximação de primeira ordem
    #aplica a extrapolaçao
    rich = richardson(r)
    return rich[n-1,n-1] # R_{n,n}



def QuadGauss(f,a,b,n=5):
    # implementado para n=5
    def h(t): 
        return f( ( (b-a)*t + b+a )/2 ) * (b-a) / 2
    x = [-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459] 
    c = [0.236926885, 0.4786286705, 0.5688888889, 0.4786286705, 0.236926885] 
    res = 0
    for i in range(len(x)):
        K = c[i]*h(x[i])
        #print(h(x[i]))
        res += K
    return res


#######################################################################
#######################################################################
#######################################################################

def intSin(f,n,method):
    pi = np.pi
    def h(x): return f(x) * np.sin(n*x)
    return method(h,-pi,pi)

def intCos(f,n,method):
    pi = np.pi
    def h(x): return f(x) * np.cos(n*x)
    return method(h,-pi,pi)
    

def fourier(method,f):
    pi = np.pi
    m = 6

    a = [method(f,-pi,pi)/(2*pi)]
    b = [0]
    for i in range(1,m):
        ai = intCos(f,i,method)/pi
        bi = intSin(f,i,method)/pi
        a.append(ai)
        b.append(bi)
    
    def FS(x):
        return sum([ a[i] * np.cos(i*x) + b[i] * np.sin(i*x) for i in range(m) ])

    x =  np.linspace(-pi,pi,100)
    fx = f(x)
    FSx = FS(x) 
    print(np.mean(abs(fx - FSx)))
    plotmult([f,FS],[-pi,pi])
    #return {'a':a,'b':b}









def main():
    def f(x): return np.sin(2*x) + abs(x)
    def method1(f,a,b): return CompositeSimpsonRule(f,a,b,100)
    def method2(f,a,b): return RombergAlgorithm(f,a,b,10)
    def method3(f,a,b): return QuadGauss(f,a,b,5)
    for method in [method1,method2,method3]:
        fourier(method,f)
    
main()
