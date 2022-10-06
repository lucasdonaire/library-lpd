# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Definindo as funções

# splines naturais

class NaturalCubicSpline:
    def __init__(self, lx, ly):
        self.lx = lx
        self.ly = ly
        self.n = len(lx)
        self.a = self.ly[:-1]
        self.b, self.c, self.d = self.gera_spline()
        self.coefs = [np.array(self.a), self.b, self.c, self.d]
    def gera_spline(self):
        # implementação do algorítmo 3.4
        h = list()
        for i in range(self.n - 1):
            h.append(self.lx[i + 1] - self.lx[i])
        alpha = [0.0]
        for i in range(1, self.n - 1):
            res = (3 * (self.ly[i + 1] - self.ly[i]) / h[i]) - ( 3 * (self.ly[i] - self.ly[i - 1]) / h[i - 1] )
            alpha.append(res)
        l = [1.0]
        u = [0.0]
        z = [0.0]
        for i in range(1, self.n - 1):
            l.append(2 * (self.lx[i + 1] - self.lx[i - 1]) - (h[i - 1] * u[i - 1]))
            u.append(h[i] / l[i])
            z.append((alpha[i] - h[i - 1] * z[i - 1]) / l[i])
        l.append(1.0)
        z.append(0.0)
        b = np.array([0.0 for i in range(self.n)])
        c = np.array([0.0 for i in range(self.n)])
        d = np.array([0.0 for i in range(self.n)])
        for j in range(self.n - 2, -1, -1):
            c[j] = z[j] - u[j] * c[j + 1]
            b[j] = (self.ly[j + 1] - self.ly[j]) / h[j] - h[j] * ( c[j + 1] + 2 * c[j] ) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])
        return b[:-1], c[:-1], d[:-1]

    def polinom(self, p):
        # P(x) aplicado em x=p
        if p < self.lx[0] or p > self.lx[self.n - 1]:
            return 0
        for i in range(self.n - 1):
            if p >= self.lx[i] and p <= self.lx[i+1]:
                X = p - self.lx[i]
                return (  self.a[i] + self.b[i] * X + self.c[i] * X ** 2 + self.d[i] * X ** 3 )


# splines fixados

class ClampedCubicSpline: 
    def __init__(self, lx, ly, FPO, FPN):
        self.lx = lx
        self.ly = ly
        self.n = len(lx)
        self.a = self.ly[:-1]
        self.FPO = FPO
        self.FPN = FPN
        self.b, self.c, self.d = self.gera_spline()
        self.coefs = [np.array(self.a), self.b, self.c, self.d]
    def gera_spline(self):
        # implementação do algorítmo 3.5
        h = list()
        for i in range(self.n - 1):
            h.append(self.lx[i + 1] - self.lx[i])
        alpha = [3*(self.ly[1]-self.ly[0])/h[0] - 3*self.FPO]
        for i in range(1,self.n-1):
            res = (3 * (self.ly[i + 1] - self.ly[i]) / h[i]) - (3 * (self.ly[i] - self.ly[i - 1]) / h[i - 1])
            alpha.append(res)
        alpha.append(3*self.FPN - 3*(self.ly[self.n-1]-self.ly[self.n-2])/h[self.n-2])
        l = [2*h[0]]
        u = [0.5]
        z = [alpha[0]/l[0]]
        for i in range(1, self.n - 1):
            l.append(2 * (self.lx[i + 1] - self.lx[i - 1]) - (h[i - 1] * u[i - 1]))
            u.append(h[i] / l[i])
            z.append((alpha[i] - h[i - 1] * z[i - 1]) / l[i])
        l.append(h[self.n-2]*(2-u[self.n-2]))  ###
        z.append((alpha[self.n-1]-h[self.n-2]*z[self.n-2])/l[self.n-1])

        b = np.array([0.0 for i in range(self.n)])
        c = np.array([0.0 for i in range(self.n)])
        d = np.array([0.0 for i in range(self.n)])
        c[self.n-1] = z[self.n-1]

        for j in range(self.n - 2, -1, -1):
            c[j] = z[j] - u[j] * c[j + 1]
            b[j] = (self.ly[j + 1] - self.ly[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])
        return b[:-1], c[:-1], d[:-1]


    def polinom(self, p):
         # P(x) aplicado em x=p
        if p < self.lx[0] or p > self.lx[self.n - 1]:
            return 0
        for i in range(self.n-1):
            if p >= self.lx[i] and p <= self.lx[i+1]:
                X = p - self.lx[i]
                return self.a[i] + self.b[i] * X + self.c[i] * X ** 2 + self.d[i] * X ** 3


# polinômio interpolador por diferenças divididas

class DividedDiferences:
    def __init__(self, x, y):
        # x vetor de mesmo tamanho que y
        self.x = np.array(x,dtype=np.float64)
        self.y = np.array(y,dtype=np.float64)
        self.n = len(x)
        f = np.zeros((self.n, self.n))
        for k in range(self.n):
            f[k, 0] = self.y[k]
        # algorítmo 3.2
        for i in range(1, self.n):
            for j in range(1, i + 1):
                f[i, j] = (f[i, j - 1] - f[i - 1, j - 1]) / (self.x[i] - self.x[i - j])
        self.coefs = f

    def polinom(self, p):
        soma = 0
        for i in range(self.n):
            res = self.coefs[i, i]
            for j in range(i):
                res *= p - self.x[j]
            soma += res
        return soma



# Aplicação 1
### Ruddy duck in flight


def duck():
    print('_____________________')
    print('RUDDY DUCK IN FLIGHT')
    X = [0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3]
    Y = [1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25]

    patoSpline = NaturalCubicSpline(X,Y)
    patoPolinomio = DividedDiferences(X,Y)

    Xbase = np.linspace(0.9,13.3,100000) # uso o método linspace para criar um vetor com xs equiespaçados para fazer o gráfico
    YSpline = [patoSpline.polinom(x) for x in Xbase]
    YPolinomio = [patoPolinomio.polinom(x) for x in Xbase]

    fig1 = plt.figure(figsize = (10,5))
    fig1.suptitle('Pato - Spline e polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinomio interpolador")
    plt.plot(Xbase, YSpline, label = "Spline")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=8)
    plt.show()

    fig2 = plt.figure(figsize = (10,2))
    fig2.suptitle('Pato - Somente spline', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YSpline, label = "Spline")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    fig3 = plt.figure(figsize = (10,2))
    fig3.suptitle('Pato - Somente polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinomio interpolador")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    # coeficientes spline
    print()
    print('Pato - os coeficientes do spline são: ')
    print(pd.DataFrame({'Xj':patoSpline.lx[:-1],'Aj':patoSpline.a,'Bj':patoSpline.b,'Cj':patoSpline.c,'Dj':patoSpline.d,'j':range(len(patoSpline.a))}).set_index('j'))

    # coeficientes polinomio de newton
    print()
    print('Pato - os coeficientes do polinômio interpolador são: ')
    print(pd.DataFrame({'coeficientes':[patoPolinomio.coefs[i,i] for i in range(len(patoPolinomio.coefs))]}))



### Noble beast
def beast():
    print('_____________________')
    print('NOBLE BEAST')
    X1 = [1,2,5,6,7,8,10,13,17]
    Y1 = [3.0,3.7,3.9,4.2,5.7,6.6,7.1,6.7,4.5]
    FPO1 = 1.0
    FPN1 = -0.67

    X2 = [17,20,23,24,25,27,27.7]
    Y2 = [4.5,7.0,6.1,5.6,5.8,5.2,4.1]
    FPO2 = 3.0
    FPN2 = -4.0

    X3 = [27.7,28,29,30]
    Y3 = [4.1,4.3,4.1,3.0]
    FPO3 = 0.33
    FPN3 = -1.5

    X = [1,2,5,6,7,8,10,13,17,20,23,24,25,27,27.7,28,29,30]
    Y =  [3.0,3.7,3.9,4.2,5.7,6.6,7.1,6.7,4.5,7.0,6.1,5.6,5.8,5.2,4.1,4.3,4.1,3.0]

    cachorro1 = ClampedCubicSpline(X1,Y1,FPO1,FPN1)
    cachorro2 = ClampedCubicSpline(X2,Y2,FPO2,FPN2)
    cachorro3 = ClampedCubicSpline(X3,Y3,FPO3,FPN3)


    def splineCachorro(x):
        if x <= 17:
            return cachorro1.polinom(x)
        if x <= 27.7:
            return cachorro2.polinom(x)
        else:
            return cachorro3.polinom(x)

    cachorroPolinomio = DividedDiferences(X,Y)

    Xbase = np.linspace(1,30,30000)
    YSpline = [splineCachorro(x) for x in Xbase]
    YPolinomio = [cachorroPolinomio.polinom(x) for x in Xbase]

    fig1 = plt.figure(figsize = (10,5))
    fig1.suptitle('Cachorro - Spline e polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinômio interpolador")
    plt.plot(Xbase, YSpline, label = "Splines")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    fig2 = plt.figure(figsize = (10,5))
    fig2.suptitle('Cachorro - Polinômio interpolador a partir de x=5 e spline', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase[4150:], YPolinomio[4150:], label = "Polinômio interpolador")
    plt.plot(Xbase, YSpline, label = "Splines")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()
    
    fig3 = plt.figure(figsize = (10,2))
    fig3.suptitle('Cachorro - Somente spline', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YSpline, label = "Splines")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    fig4 = plt.figure(figsize = (10,2))
    fig4.suptitle('Cachorro - Somente polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinômio interpolador")
    plt.scatter(X, Y, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    # coeficientes
    print()
    print('Cachorro - os coeficientes do primeiro spline são: ')
    print(pd.DataFrame({'Xj':cachorro1.lx[:-1],'Aj':cachorro1.a,'Bj':cachorro1.b,'Cj':cachorro1.c,'Dj':cachorro1.d,'j':range(len(cachorro1.a))}).set_index('j'))
    print()
    print('Cachorro - os coeficientes do segundo spline são: ')
    print(pd.DataFrame({'Xj':cachorro2.lx[:-1],'Aj':cachorro2.a,'Bj':cachorro2.b,'Cj':cachorro2.c,'Dj':cachorro2.d,'j':range(len(cachorro2.a))}).set_index('j'))
    print()
    print('Cachorro - os coeficientes do terceiro spline são: ')
    print(pd.DataFrame({'Xj':cachorro3.lx[:-1],'Aj':cachorro3.a,'Bj':cachorro3.b,'Cj':cachorro3.c,'Dj':cachorro3.d,'j':range(len(cachorro3.a))}).set_index('j'))

    # coeficientes polinomio de newton
    print()
    print('Cachorro - os coeficientes do polinômio interpolador são: ')
    print(pd.DataFrame({'coeficientes':[cachorroPolinomio.coefs[i,i] for i in range(len(cachorroPolinomio.coefs))]}))

### Aplicação 2
def robot():
    print('_____________________')
    print('ROBÔ')
    t = [1,2,3,4,5,6]
    theta = [1.0,1.25,1.75,2.25,3.0,3.15]

    roboSpline = ClampedCubicSpline(t,theta,0.125,-0.15)
    roboPolinomio = DividedDiferences(t,theta)

    Xbase = np.linspace(1,6,10000)
    YSpline = [roboSpline.polinom(x) for x in Xbase]
    YPolinomio = [roboPolinomio.polinom(x) for x in Xbase]
    

    fig1 = plt.figure(figsize = (10,5))
    fig1.suptitle('Robô - Spline e polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinômio interpolador")
    plt.plot(Xbase, YSpline, label = "Splines")
    plt.scatter(t, theta, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    fig2 = plt.figure(figsize = (10,5))
    fig2.suptitle('Robô - Somente spline', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YSpline, label = "Splines")
    plt.scatter(t, theta, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    fig3 = plt.figure(figsize = (10,5))
    fig3.suptitle('Robô - Somente polinômio interpolador', fontsize = 15)
    plt.xlabel('x', fontsize = 15)
    plt.ylabel('f(x)', fontsize = 15)
    plt.grid()
    plt.plot(Xbase, YPolinomio, label = "Polinômio interpolador")
    plt.scatter(t, theta, label = "Pontos", color = "r")
    plt.legend(fontsize=10)
    plt.show()

    print()
    print('Robô - os coeficientes do spline são: ')
    print(pd.DataFrame({'Xj':roboSpline.lx[:-1],'Aj':roboSpline.a,'Bj':roboSpline.b,'Cj':roboSpline.c,'Dj':roboSpline.d,'j':range(len(roboSpline.a))}).set_index('j'))


    # coeficientes polinomio de newton
    print()
    print('Robô - os coeficientes do polinômio interpolador são: ')
    print(pd.DataFrame({'coeficientes':[roboPolinomio.coefs[i,i] for i in range(len(roboPolinomio.coefs))]}))

    print()
    print('Robô - A aproximação da posição do robô em t=1.5 é: \n f(1.5) = ',end='')
    print(roboSpline.polinom(1.5))



def main():
    duck()
    beast()
    robot()

main()