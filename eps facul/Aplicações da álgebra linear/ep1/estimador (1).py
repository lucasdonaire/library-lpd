#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:52:34 2022

@author: lucasdonaire
"""


from scipy.sparse.linalg import spsolve as sp
from scipy.sparse import csc_matrix
import scipy
import numpy as np
import math as m
import matplotlib.pyplot as plt
import pandas as pd


def u(x): #função para nos dar condições de contorno.
    return m.exp(m.cos(x))

def rhs(h, k): #função do "right hand side" de -u''(x) = (cos(x) - sin^2(x))*exp(cos(x))
    a = 0
    x_k = a + h*k
    #print(f'xk = {x_k}, k = {k}')
    return (m.cos(x_k) - (m.sin(x_k))**2)*(m.exp(m.cos(x_k)))


def calc(n):
    a = 0
    b = 2*m.pi
    h = (b-a)/n
    
    f_k = np.zeros((n-1, 1))
    
    #print('\n Aqui inicia-se o povoamente do vetor coluna f_k \n')
    
    for i in range(n-1):
        f_k[i] = rhs(h,i+1)
   
        
    #print(f' O vetor f_k fora povoado com: {n-1} entradas')
        
    
    #print(f'\n Aqui inicia-se a montagem da matriz esparsa, de bandas, e tridiagonal de dimensão: {n-1}x{n-1} \n')
    
    u_k = csc_matrix((n-1, n-1), dtype = np.float64)
    u_k = scipy.sparse.lil_matrix(u_k) # formato do scipy de matrizes esparsas, mas bom para fazer operações e atribuições
    
    # popula u_k
    tp = np.array([1,-2,1])
    tm = np.array([-1,16,-30,16,-1])
    for i in range(n-1):
        if i in [0,1,n-3,n-2]:
            for j in range(3):
                #u_k[i,-1+j+pula] = tp[j]
                #print(i,j,'||||||||',tp[j],'-----> [',i,-1+j+i, ']')
                if -1+j+i >= 0 and -1+j+i < n-1:
                    u_k[i,-1+j+i] = tp[j]
        else:
            for j in range(5):
                u_k[i,-2+j+i] = tm[j]
            
        

    u_k = csc_matrix(u_k)
    
    
    #### ajustando o vetor b (Ax=b)
    #b = -h**2 * fk * [2,2,12,12,12,...,12,12,2,2]+ [e,0,0,0,...,0,0,0,e]
    f_k = f_k*(-(h**2))
    vmult = np.array([[12]]*(n-1))
    vmult[0] = 2
    vmult[n-2] = 2
    f_k = f_k * vmult
    ve = np.array([[0.0]]*(n-1)).copy()
    ve[0] = np.e
    ve[n-2] = np.e
    f_k = f_k - ve
    
    
    
    #### calculando o resultando e adicionando as bordas
    vetor = sp(u_k, f_k) # resolve o Ax=b, no caso u_k x = f_k
    res = [np.e]  
    res.extend(vetor)
    res.extend([np.e])

    ### calculando y nos pontos com a função original para fins de teste
    y = np.array([None]*(n+1))
    for i in range(n+1):
        x = a + h*i
        y[i] = u(x)
    
        
    return res, y


def testes():
    
    d = {'n':[],
         'h':[],
         '||e(h)||2':[],
         '||e(h)||inf':[],
         'p_2':[],
         'p_inf':[],
       }
    
    for i in range(4): # altere o range para testar mais valores
        n = 2**(i+7)
        fhat, fx = calc(n) 
        dif = fhat-fx
        h = 2*m.pi/n
        eps = max(abs(dif))
        epe = np.linalg.norm(dif)
        eix = np.linspace(0, 2*m.pi, len(dif)-2)
        plt.plot(eix, dif[1:-1])
        d['n'].append(n)
        d['h'].append(h)
        d['||e(h)||inf'].append(eps)
        d['||e(h)||2'].append(epe)
        if d['p_inf'] == []:
            d['p_inf'].append('-')
        else:
            p = eps/d['||e(h)||inf'][len(d['||e(h)||inf'])-2]
            d['p_inf'].append(np.log2(1/p))
            
        if d['p_2'] == []:
            d['p_2'].append('-')
        else:
            p = epe/d['||e(h)||2'][len(d['||e(h)||2'])-2]
            d['p_2'].append(np.log2(1/p))
        
    df = pd.DataFrame(d)
    print(df)

testes()