#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:15:58 2021

@author: Jorge
"""

import math
#import Matrix as mtx
import fractions as fc
import numpy as np
import statistics as stat
normal = stat.NormalDist(0,1)
import matplotlib.pyplot as plt

'''
x= np.linspace(0, 6, 100)
y= np.sin(x)
    

plt.figure()
plt.plot(x,y,'bh',label='',linewidth= 1.1)
plt.legend()
'''



esp = '-=-' * 15


# FRACTIONS
def sim():
    c = (input('sim: '))
    c = fc.Fraction(c)
    c = float(c)
    print(c)
#----------------------------------------------

def binom(n, x, p):
    """"
    acontecem x eventos de n, com a probabilidade p
    """
    q = 1 - p
    binom1 = p**x * q**(n - x)
    binom2 = comb(n,x)
    prob1 = binom1 * binom2        
    print(prob1)
    return prob1

def geom(p,x):
    """
    com a probabilidade p, o evento ocorre até o sucesso
    qual a chance dele ocorrer x vezes?
    """
    q = 1 - p
    i = 1
    soma = 0
    while i <= x:
        prob = p * q**(i-1)
        print(f'probabilidade de x = {i} é {prob}')
        soma = soma + prob        
        print(f'a soma acumulada até {i} é de {soma}')
        print()
        i = i + 1
    
    return prob

def fat(n):
    x = 1
    z = 1
    while n>0:
        z = x * z
        x = x + 1   
        n = n - 1 
    return z

def comb(n,x):
    """
    Combinação de n tomado x a x
    """
    combin = fat(n)//(fat(x)*fat(n - x))
    return combin

def poiss(l,x):
    """
    Distribuição de poisson, l = lambda
    """
    e = 2.7182818284590452353602874
    fatx = fat(x)
    prob = (e**(-l) * l**(x))/fatx
    print(prob)
    return prob

def vardisc():
    print('1 --> dando quantas vezes aparece')
    print('2 --> dando a probabilidade')
    p = int(input('1 ou 2: '))
    if p == 1:
        vardisc1()
    if p == 2:
        vardisc2()
       
def vardisc1():
    n5 = int(input('Digite o total de números: '))
    p = int(input('Digite o total de elementos: '))
    i5 = 0
    media = 0
    media2 = 0
    somaj = 0
    while i5 < n5:
        k = float(input('Digite o x: '))
        j = int(input('Digite quantas vezes x aparece; '))
        somaj = somaj + j
        media = media + (k*j)/p
        media2 = media2 + k*k*(j/p)
        i5 = i5 + 1
    var = media2 - media**2
    dp = var**0.5
    if somaj == p:    
        print(f'A média2 é {media2}')
        print(f'A média é {media}')
        print(f'A variância é {var}')
        print(f'O desvio padrão é {dp}')
    else:
        print('nunca')
    return media
        
def vardisc2():
    n5 = int(input('Digite o total de números: '))
    i5 = 0
    media = 0
    media2 = 0
    somaj = 0
    while i5 < n5:
        k = float(input('Digite o x: '))
        j = input('Digite a probabilidade ')
        j = fc.Fraction(j)
        j = float(j)
        somaj = somaj + j
        media = media + (k*j)
        media2 = media2 + k*k*(j)
        i5 = i5 + 1
    var = media2 - media**2
    dp = var**0.5
    if somaj == 1:    
        print(f'A média2 é {media2}')
        print(f'A média é {media}')
        print(f'A variância é {var}')
        print(f'O desvio padrão é {dp}')
    else:
        print('nunca')
    return media

def arr(n,x):
    """
    Arranjo de n elementos tomados x a x
    """
    arranjo = comb(n,x)*fat(x)
    return arranjo

def pascal(m):
    """
    todas combinações de um n dado
    """
    i = 0
    soma = 0
    while i <= m:
        print(f'combinação ({m}, {i}) = {comb(m,i)} ')
        soma = soma + comb(m,i)
        i = i + 1
    print(soma)
    
def varquant():
    n = int(input('Digite o total de números: '))
    i = 0
    somax = 0
    somay = 0
    somax2 = 0
    somay2 = 0
    somaxy = 0
    while i < n:
        x = input(f' Digite x{i + 1}: ')
        x = fc.Fraction(x)
        x = float(x)
        y = input(f' Digite y{i + 1}: ')
        y = fc.Fraction(y)
        y = float(y)
        somax += x
        somay += y
        somax2 += x**2
        somay2 += y**2
        somaxy += x*y
        i += 1
    
    
    mediax = somax/n
    mediay = somay/n
    
    varx = (somax2 - (n * mediax**2))/n
    vary = (somay2 - (n* mediay**2))/n
    dpx = varx**0.5
    dpy = vary**0.5
    covxy = (somaxy - (n * mediax * mediay))/n
    corrxy = covxy/(dpx*dpy)
    beta = covxy/varx
    alfa = mediay - beta*mediax

    print(f'a mediax é {mediax}')
    print(f'a mediay é {mediay}')
    print(f'a somax é {somax}')
    print(f'a somay é {somay}')
    print(f'a somaxy é {somaxy}')
    print(f'a somax2 é {somax2}')
    print(f'a somay2 é {somay2}')
    print(f'a varx é {varx}')
    print(f'o dpx é {dpx}')
    print(f'a vary é {vary}')
    print(f'o dpy é {dpy}')
    print(f'a covxy é {covxy}')
    print(f'a corrxy é {corrxy}')
    print(f'o alfa é {alfa}')
    print(f'o beta é {beta}')
       
def unif(a, b, x=0):
    print(f'valor de f é {1/(b-a)}')
    print(f'esperança é {(a+b)/2}')
    print(f'var é { (b-a)**2 /12}')
    #x = float(input('digite x entre a e b: '))
    if a<= x <=b:    
        ac = (x-a)/(b-a)
        
    elif x < a:
        ac = 0
        
    else:
        ac = 1
        
    print(f'acumulado ate x temos {ac}')
    
def trian(a,c,b,x=0):
    print(f'esperança é {(a+b+c)/3}')
    var = (1/18) * (a**2 + b**2 + c**2 - a*b - b*c - c*a)
    print(f'var é {var}')
    if x < a or x > b :
        fx = 0
    elif a <= x <= c:
        fx = 2*(x-a)/((b-a)*(c-a))
    elif c < x <= b:
        fx = 2*(b-x)/((b-a)*(b-c))
        
    print(f'f({x}) = {fx}')
    
def dexp(l, x):
    e = math.e
    fx = l * e**(-l*x)
    print(f'valor de f é {fx}')
    print(f'esperança é {1/l}')
    print(f'var é {1/(l**2)}')
    print(f'a funcao acumulada é {1 - e**(-l*x)}')
    
def lcsoma(m, v, n, a=0, b=1):
    nm = n*m
    nv = n*v
    print(f'nova media é {nm}')
    print(f'nova var é {nv}')
    za = (a - nm)/(nv**0.5)
    zb = (b - nm)/(nv**0.5)
    
    print(f'za = {za}')
    print(f'zb = {zb}')
      
def lcmedia(m, v, n, a=0, b=1):
    nm = m
    nv = v/n
    print(f'nova media é {nm}')
    print(f'nova var é {nv}')
    za = (a - nm)/(nv**0.5)
    zb = (b - nm)/(nv**0.5)
    print(f'za = {za}')
    print(f'zb = {zb}')
    
def apbpn(n,p,a,b):
    print(f'é boa se ({n*p*(1-p)})>3')
    pa = (a -n*p)/((n*p*(1-p))**0.5)
    pb = (b -n*p)/((n*p*(1-p))**0.5)
    print(f'za = {pa}')
    print(f'zb = {pb}')
    
    print('---------------------')
    print('com correção de continuidade: ')
    pa = (a -n*p -0.5)/((n*p*(1-p))**0.5)
    pb = (b -n*p + 0.5)/((n*p*(1-p))**0.5)
    print(f'za = {pa}')
    print(f'zb = {pb}')
       
def printada(mt, lx, ly, somax, somay):
    print()
    m = []
    for i in range(len(lx)):
            m += [len(str(lx[i]))]
    tam = max(m)
    
    print(' ' * (tam+3), end ='' )
    falt1 = []
    for i in mt:
        falt1 += [len(str(i))]
    maxfalt = max(falt1)
    falt2 = []
    for i in range(len(falt1)):
        falt2 += [maxfalt - falt1[i]]
    for i in ly:
        print(i, end = '\t')
    print('')
    print('-----------------------------------')
    for j in range(len(lx)):
        print(lx[j], end = ' | ')
        print(mt[j], end = (' '*falt2[j]+'| '))
        print(somax[j])
    
    print('-----------------------------------')
    print(' ' * (tam+3), end ='' )
    for i in somay:
        print(i, end = '\t')
        
def matrizada(l, c):
    val = 0
    mt = l *[val]
    for i in range(l):
        mt[i] = c*[val] 
    for i in range(l):
        for j in range(c):
            valor = input(f"Digite elem [{i}][{j}]: ")
            valor = fc.Fraction(valor)
            valor = float(valor)
            mt[i][j] = valor
    return mt

def bid_inp():
    x = int(input('Digite x: '))
    y = int(input('Digite y: '))  
    lx = []
    ly = []
    for i in range(x):
        x0 = float(input(f'Digite x{i}: '))
        lx += [x0]
    for j in range(y):
        y0 = float(input(f'Digite y{j}: '))
        ly += [y0]
    mt = matrizada(x, y) 
    bid(mt, lx, ly)
    
def bid(mt, lx, ly):
    x = len(mt)
    y = len(mt[0])
    # -------------------------
    # x
    somax = []
    mtx.exiba_matriz(mt)
    print(esp)
    for i in range(x):
        somax += [sum(mt[i])]
    print(f'lx = {lx}')
    print(f'somax = {somax}')
    ex = 0
    ex2 = 0
    for i in range(x):
        vx = somax[i] * lx[i]
        ex += vx
        ex2 += (vx * lx[i])
    print(f'ex = {ex}')
    print(f'ex2 = {ex2}')
    varx = ex2 - ex**2
    print(f'varx = {varx}')
    dpx = varx**0.5
    print(f'dpx = {dpx}')
    print(esp)
    # --------------------------
    # y
    
    somay = []
    for i in range(y):
        l = []
        for j in range(x):
            l += [mt[j][i]]
        somay += [sum(l)] 
    print(f'ly = {ly}')
    print(f'somay = {somay}')  
    ey = 0
    ey2 = 0
    for i in range(y):
        vy = somay[i] * ly[i]
        ey += vy
        ey2 += (vy * ly[i])
    print(f'ey = {ey}')
    print(f'ey2 = {ey2}')
    vary = ey2 - ey**2
    print(f'vary = {vary}')
    print(esp)
    dpy = vary**0.5
    print(f'dpy = {dpy}')
    print(esp)
    
    #--------------------------
    # juntos
    
    lxdy = []
    for i in range(y):
        pxdy = 0
        for j in range(x):  
            pxdy += lx[j] * mt[j][i]
        lxdy += [pxdy / somay[i]]
    print(f'lxdy = {lxdy}')
    
    lydx = []
    for i in range(x):
        pydx = 0
        for j in range(y):  
            pydx += ly[j] * mt[i][j]
        lydx += [pydx / somax[i]]
    print(f'lydx = {lydx}')
    
    
    
    
    
    
    exy = 0
    for i in range(x):
        for j in range(y):
            vxy = mt[i][j] * lx[i] * ly[j]
            exy += vxy
            
    print(f'exy = {exy}')
    covxy = exy - (ex * ey)
    print(f'covxy = {covxy}')
    corrxy = covxy / (dpx * dpy)
    print(f'corrxy = {corrxy}')
    print(esp)
    
    printada(mt,lx,ly,somax,somay)  
    
    
def minquad(lx,ly,f):
    '''
    lx/ly = lista dos valores observados
    Y = f(x) + erro
    '''
    soma = 0
    for i in range(len(lx)):
        v = (ly[i] - f(lx[i]))**2
        soma += v
    return soma
 


    
 
    
 
soma = 0
p = 2/3
n = 100
for i in(42,59):
    soma += binom(n, i, p)

print()
print(soma)
    
        
        
        
        
        


        
        
        
    
    
        