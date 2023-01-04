import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# função para plotar resultados
def plotmult(listF, interval=[0,10],names=['' for i in range(100)]):
    names = iter(names)
    x = np.linspace(interval[0], interval[1], 1000)
    plt.figure()
    for f in listF:
        y = list()
        for i in range(len(x)):
            y.append(f(x[i]))
        y = np.array(y)
        plt.plot(x, y, label = next(names))
    plt.legend()
    plt.show()


def CompositeSimpsonRule(f,a,b,n):
    # n par
    # algoritmo 4.1
    # computa a integral de f em [a,b] com n pontos pela regra de simpson composta
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


def richardsonExtrapolation(LN1):
    # recebe LN1 = [N1(h), N1(h/2), ..., N1(h / 2^(n-1))]
    # onde o erro f - N1(h) é da forma K1*h^2 +k2*h^4 + ... 
    # retorna tabela/matriz com a extrapolação de richardson, onde M[n-1,n-1] é a melhor aproximação
    n = len(LN1)
    M = np.zeros((n,n))
    for j in range(n):
        M[j,0] = LN1[j]
    
    for i in range(1,n):
        for j in range(i,n):
            res = M[j,i-1]+(M[j,i-1]-M[j-1,i-1])/(4**(i)-1)
            M[j,i] = res
    
    return M


def RombergAlgorithm(f,a,b,n):
    # computa a integral de f em [a,b] com N=1,2,...,2^n pontos e aplica a extrapolação de richardson
    # algoritmo 4.2 modificado (extrapolação de richardson está em outra função)
    h = [(b-a)/2**(k-1) for k in range(1,n+1)]
    r = [h[0]*(f(a)+f(b))/2] # r: lista de aproximações pela regra do trapézio
    
    for k in range(1,n):
        soma = sum( [f(a + (2*i-1)*h[k]) for i in range(1,2**(k-1)+1) ] )
        r.append( (r[k-1] + h[k-1] * soma)/2 ) # calcula aproximação de primeira ordem usando regra do trapézio
    
    rich = richardsonExtrapolation(r) #aplica a extrapolaçao
    return rich[n-1,n-1] # R_{n,n}



def gaussQuadrature(f,a,b):
    # computa a integral de f em [a,b]  com n=5 pela quadratura de Gauss
    # implementado para n=5
    def h(t): 
        return f( ( (b-a)*t + b+a )/2 ) * (b-a) / 2  # transformação 

    x = [-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459] 
    c = [0.236926885, 0.4786286705, 0.5688888889, 0.4786286705, 0.236926885] 

    res = sum( [ c[i]*h(x[i]) for i in range(len(x)) ] )
    return res


#######################################################################
#######################################################################
#######################################################################


def intSin(f,n,method): # integral de f(x)sin(nx) em [-pi,pi] -> para usar na série de fourier
    pi = np.pi
    def h(x): return f(x) * np.sin(n*x)
    return method(h,-pi,pi)

def intCos(f,n,method): # integral de f(x)cos(nx) em [-pi,pi] -> para usar na série de fourier
    pi = np.pi
    def h(x): return f(x) * np.cos(n*x)
    return method(h,-pi,pi)
    

def fourier(method,f,m):
    pi = np.pi

    a = [method(f,-pi,pi)/(2*pi)]
    b = [0]
    for i in range(1,m+1):
        ai = intCos(f,i,method)/pi
        bi = intSin(f,i,method)/pi
        a.append(ai)
        b.append(bi)
    for i in range(m+1):
        print(f' {a[i]:f} * np.cos({i}x) + {b[i]:f} * np.sin({i}x)' )

    def FS(x):  # fourier series
        return sum([ a[i] * np.cos(i*x) + b[i] * np.sin(i*x) for i in range(m+1) ])

    
    x =  np.linspace(-pi,pi,1000)
    
    dif = abs(f(x) - FS(x))
    medio = np.mean(dif)
    mxm = max(dif)
        
    return {'media':medio,'maximo':mxm,'FS':FS,'f':f}









def aplic1():
    #listFPlot = []
    #nomesPlot = []
    res = {'função':[],'média Simpson':[],'máximo Simpson':[],'média Romberg':[],'máximo Romberg':[], 'média Gauss':[],'máximo Gauss':[]}
    def method1(f,a,b): return CompositeSimpsonRule(f,a,b,100)
    def method2(f,a,b): return RombergAlgorithm(f,a,b,10)
    def method3(f,a,b): return gaussQuadrature(f,a,b)
    for k in [1,2,3,5,10]:
        def sinKx(x): return np.sin(k*x) 
        def cosKx(x): return np.cos(k*x) 
        def cosPlusSin(x): return np.sin(k*x) + np.cos(k*x)
        #listFPlot.append(cosPlusSin)
        #nomesPlot.append('f')
        res['função'].extend([ f'sin({k}x)',f'cos({k}x)',f'sin({k}x) + cos({k}x)' ])
        for method,nameMethod in [(method1,'Simpson'),(method2,'Romberg'),(method3,'Gauss')]:
            dsin = fourier(method,sinKx,10)
            dcos = fourier(method,cosKx,10)
            dsum = fourier(method,cosPlusSin,10)
            #listFPlot.append(dsum['FS'])
            #nomesPlot.append(nameMethod)
            res[f'média {nameMethod}'].extend([ dsin['media'],dcos['media'],dsum['media'] ])
            res[f'máximo {nameMethod}'].extend([ dsin['maximo'],dcos['maximo'],dsum['maximo'] ])    
    print(pd.DataFrame(res))
    #plotmult(listFPlot,[-np.pi,np.pi],nomesPlot)








def aplic2():
    # listFPlot = []
    # nomesPlot = []
    res = {'função':[],'média Simpson':[],'máximo Simpson':[],'média Romberg':[],'máximo Romberg':[], 'média Gauss':[],'máximo Gauss':[]}
    def method1(f,a,b): return CompositeSimpsonRule(f,a,b,100)
    def method2(f,a,b): return RombergAlgorithm(f,a,b,10)
    def method3(f,a,b): return gaussQuadrature(f,a,b)
    for k in [2,5,10]:
        def mon(x): return x**k
        def poli(x): return x**k + 2*x**(k-1)
        #listFPlot.append(poli)
        #nomesPlot.append('f')
        res['função'].extend([ f'x^{k}',f'x^{k}+2x^{k-1}'])
        for method,nameMethod in [(method1,'Simpson'),(method2,'Romberg'),(method3,'Gauss')]:
            dmon = fourier(method,mon,10)
            dpoli = fourier(method,poli,10)
            #listFPlot.append(dpoli['FS'])
            #nomesPlot.append(nameMethod)
            res[f'média {nameMethod}'].extend([ dmon['media'],dpoli['media'] ])
            res[f'máximo {nameMethod}'].extend([ dmon['maximo'],dpoli['maximo'] ])
        
    res['função'].extend([ 'e^x','|x|','log(|x|+1)'])
    def logmod(x): return np.log(abs(x)+1)
    # listFPlot.append(logmod)
    # nomesPlot.append('f')
    for method,nameMethod in [(method1,'Simpson'),(method2,'Romberg'),(method3,'Gauss')]:
        dexp = fourier(method,np.exp,10)
        dabs = fourier(method,abs,10)
        dlogmod = fourier(method,logmod,10)
        # listFPlot.append(dlogmod['FS'])
        # nomesPlot.append(nameMethod)
        res[f'média {nameMethod}'].extend([ dexp['media'],dabs['media'],dlogmod['media'] ])
        res[f'máximo {nameMethod}'].extend([ dexp['maximo'],dabs['maximo'],dlogmod['maximo'] ]) 
    
    # plotmult(listFPlot,[-np.pi,np.pi],nomesPlot)
    print(pd.DataFrame(res))







def aplic3():
    # listFPlot = []
    # nomesPlot = []
    res = {'N':[],'média Simpson':[],'máximo Simpson':[],'média Romberg':[],'máximo Romberg':[], 'média Gauss':[],'máximo Gauss':[]}
    def method1(f,a,b): return CompositeSimpsonRule(f,a,b,100)
    def method2(f,a,b): return RombergAlgorithm(f,a,b,10)
    def method3(f,a,b): return gaussQuadrature(f,a,b)
    def supf(x): 
        if x < 0: return -1
        elif x > 0: return 1
        else: return 0
    def f(x): 
        if type(x) in [float, np.float64]: return supf(x)
        else: return np.array([supf(x_) for x_ in x])
    # listFPlot.append(f)
    # nomesPlot.append('f')
    for k in range(1,30,3):
        res['N'].append(k)
        for method,nameMethod in [(method1,'Simpson'),(method2,'Romberg'),(method3,'Gauss')]:
            df = fourier(method,f,k)
            # listFPlot.append(df['FS'])
            # nomesPlot.append(f'N = {k}')
            res[f'média {nameMethod}'].append( df['media'] )
            res[f'máximo {nameMethod}'].append( df['maximo'] )
    
    
    # plotmult(listFPlot,[-np.pi,np.pi],nomesPlot)
    print(pd.DataFrame(res))



def main():
    # print('=======================')
    # print('APLICAÇÃO 1')
    # aplic1()
    # print('=======================')
    # print('APLICAÇÃO 2')
    # aplic2()
    # print('=======================')
    # print('APLICAÇÃO 3')
    # aplic3()
    # return
    def f(x): return np.sin(x + np.pi/4) 
    def method(f,a,b): return RombergAlgorithm(f,a,b,10)
    df = fourier(method,f,5)
    plotmult([df['f'],df['FS']],[-np.pi,np.pi],['f','fs'])
main()
