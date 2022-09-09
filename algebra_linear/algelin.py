#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:39:17 2021

@author: Jorge
"""
#! pip install sympy

import math
import numpy as np
from sympy import symbols, Matrix
x = symbols("x")
'''

n = [[1,2,3],[4,5,6],[7,8,9]]
n = np.matrix(n)
print(np.linalg.det(n))


mm = ([[1,2],[2,9]])
mm = np.matrix(mm)
print(np.linalg.det(mm))

m = []
s = []
if False:
    nl = int(input('digite o numero de linhas/variaveis: '))
    for i in range(nl):
        s += [float(input(f'Digite o resultado da linha {i + 1}: '))]
        mx = []
        for j in range(nl):
            mx += [float(input(f'digite o termo {j + 1} da linha {i + 1}: '))]  
        m += [mx]
elif False:
    m = [[1.0, 1.0], [1.0, -1.0]]
    s = [3.0, 1.0]
    nl = 2
    
else:
    m = [[1.0, 1.0, 2.0], [1.0, -1.0, 3.0], [-1, 3, 2]]
    s = [3.0, 1.0, -4.0]
    nl = 3
    
    
D = np.linalg.det(m)
print('==========')
print(f'm = {m}')
print(f'det(m) = {D}')
print(f's = {s}')
print('=============')

mc = m[:]
lres = []
for i in range(nl):
    mzada = []
    for k in range(len(m)):
        mzada += [mc[k][:]]
    

    #print(f'm = {m}')
    #print(f'mzada inicial = {mzada}')
    # cada variavel começa a rodar aqui
    for j in range(nl):
        mzada[j][i] = s[j]
        
    #print(f'--{i}--')
    #print(mzada)
    dn = np.linalg.det(mzada)
    var = dn/D
    lres += [var]
    print(f' o valor da variavel {i+1} é {var}')
        
    
print('========')
for i in range(nl):
    soma = 0
    for j in range(nl):
        soma += m[i][j] * lres[j]
        
    print(f'resultado {i} = {soma}')
    print(f'resultado certo = {s[i]}')
    
'''

    
# ----------------------------------------------
def slin(a, b):
    '''
    duas listas, soma cada elemento
    '''
    ar(a)
    ar(b)
    
    ln = []
    for i in range(len(a)):
        ln += [a[i] + b[i]]
        
    return ln

def mlinlin(a,b):
    '''
    duas listas, multiplica cada elemento
    '''
    
    

    ln = []
    for i in range(len(a)):
        ln += [a[i] * b[i]]
        
        
        
   # print(f'lista do mlinlin = {ln}')
    return ln

def mlin(a, n):
    '''
    lista a multiplicada por n
    '''
    ln = []
    #print('---- to de mlin')
    #print(a)
    for i in range(len(a)):
        ln += [a[i] * n]
        
    return ln
        
def redlin(l): # reduzir linha
    gt = max(l)
    for i in range(len(l)):
        if l[i] != int(l[i]):
            return l
        gt = math.gcd(int(l[i]), int(gt))
      
    ln = []
    for i in range(len(l)):
        ln += [l[i]/gt]
        
    return ln
    
def esc(m1, nlin = 0, ncol = 0): #escalonar





#se quiser q printe, tira os #


    #m1 = []
    if nlin == 0:
        nlin = len(m1)
    if ncol == 0 :
        ncol = len(m1[0])
    
    if False:
        for i in range(nlin):
            l1 = []
            for j in range(ncol):
                l1 += [float(input(f'Digite o termo {j+1} da linha {i+1}: '))]
            m1 += [l1]
    elif False:
       m2 = [[1.0, -2.0, -6.0, 5.0], [5.0, -6.0, -2.0, 13.0], [2.0, 0.0, 16.0, -2.0]]
       m3 = [[1.0, -2.0, -6.0, 5.0], [0.0, 1.0, 7.0, -3.0], [1,3,0,1]]
       m1 = [[2,1,0,0],[-1,0,0,1],[-1,0,1,0],[0,0,1,1]]
   
    #print(f'm1 ===== \n {m1}')
    m2 = m1[:]    
    #print(f'm2 ===== \n {m2}')
    for i in range(nlin): #cada linha, começando linha1 zerar coef 1 
        print(f'-----rodada {i+1}------')
        if nlin - i >= 2:
            if m2[i][i] == 0 and m2[i+1][i] !=0:
                print('TROQUEI')
                m2[i], m2[i+1] = m2[i+1], m2[i]
                
                
     #   print(f'm2 ===== \n {m2}')
        if max(m2[i]) == 0 and min(m2[i]) == 0:
            return m2
        
        for j in range(i+1,nlin): # zerar cada coef por vez
            m2[j] = slin(m2[j],(mlin(m2[i],(-1 * m2[j][i]/m2[i][i]))))
            
            
        print(m2)
                 
    return m2

def reduz(m2): #reduzir cada linha da matriz
    for i in range(len(m2)):
        if not (max(m2[i]) == 0 and min(m2[i]) == 0):
            m2[i] = redlin(m2[i])
    return m2
                
def slinear(): #resolve sist linear nao homogeneo
    m = []
    s = []
    if True:
        nl = int(input('digite o numero de linhas/variaveis: '))
        for i in range(nl):
            s += [float(input(f'Digite o resultado da linha {i + 1}: '))]
            mx = []
            for j in range(nl):
                mx += [float(input(f'digite o termo {j + 1} da linha {i + 1}: '))]  
            m += [mx]
        
    else:
        m = [[1.0, 1.0, 2.0], [1.0, -1.0, 3.0], [-1, 3, 2]]
        s = [3.0, 1.0, -4.0]
        nl = 3
        
        
    D = np.linalg.det(m)
    print('==========')
    print(f'm = {m}')
    print(f'det(m) = {D}')
    print(f's = {s}')
    print('=============')
    
    mc = m[:]
    lres = []
    for i in range(nl):
        mzada = []
        for k in range(len(m)):
            mzada += [mc[k][:]]
        
    
        #print(f'm = {m}')
        #print(f'mzada inicial = {mzada}')
        # cada variavel começa a rodar aqui
        for j in range(nl):
            mzada[j][i] = s[j]
            
        #print(f'--{i}--')
        #print(mzada)
        dn = np.linalg.det(mzada)
        var = dn/D
        lres += [var]
        print(f' o valor da variavel {i+1} é {var}')
            
        
    print('========')
    for i in range(nl):
        soma = 0
        for j in range(nl):
            soma += m[i][j] * lres[j]
            
        print(f'resultado {i} = {soma}')
        print(f'resultado certo = {s[i]}')
        
def slin2(m, s):  #ja poe as matrizes de input
# input (coeficientes, resultado)
    nl = len(s)
    
    D = np.linalg.det(m)
    #print('==========')
    #print(f'm = {m}')
    #print(f'det(m) = {D}')
    #print(f's = {s}')
    #print('=============')
    
    mc = m[:]
    lres = []
    for i in range(nl):
        mzada = []
        for k in range(len(m)):
            mzada += [mc[k][:]]
        
    
        #print(f'm = {m}')
        #print(f'mzada inicial = {mzada}')
        # cada variavel começa a rodar aqui
        for j in range(nl):
            mzada[j][i] = s[j]
            
        #print(f'--{i}--')
        #print(mzada)
        dn = np.linalg.det(mzada)
        #print('dn', dn)
        var = dn/D
        print(mzada)
        lres += [var]
        print(f' o valor da variavel {i+1} é {var}')
    
    return lres

def slin3(m, s):  #ja poe as matrizes de input
# input (coeficientes, resultado)
    nl = len(s)
    D = np.linalg.det(m)
    lres = []
    for i in range(nl):
        mzada = m.copy()
        mzada[:, i] = s.copy()
        dn = np.linalg.det(mzada)
        var = dn/D
        #print(mzada)
        lres += [var]
        print(f' o valor da variavel {i+1} é {var}')
    
    return lres

def resolve_coef(mat, res):
    '''
    mat = matriz q cada linha sao os vetores de Rn
    res = matriz 1 x n com o resultado
    '''

    mat2 = np.transpose(mat)
    return slin3(mat2, res)
        
def criamt_velha(lin,col): # cria matriz
    l = [0] * (lin*col)
    #print(l)
    mt = np.array(l).reshape(lin,col)
    #print(mt)
    for i in range(lin):
        for j in range(col):
            #mt = mt.copy()
            v = float(input(f'digite o termo {j+1} da linha {i+1}: '))
            print(v)
            mt[i][j] = float(v)
            
    print(mt)
    return mt
    
'''

def mudbase(B): #matriz mudanca de base Can -> B (MB = canonica)
    n = len(B.copy())
    l = [0] * (n * n)
    mt = np.array(l).reshape(n, n)
    
    #print('mt', mt)
    # mt é a matriz q vamos preencher
    can = np.identity(n)
    #print(can)
    for i in range(n):
        #print('-------------------for-------------')
        #print(B)
        #print(can[i])
        val = resolve_coef(B.copy(), can[i])
        #print(val)
        mt[i] = val
        
    return mt
    
    
    
    
    #return np.linalg.inv(B)

def mattl(Tcan, B):
    print(B, Tcan)
    M = mudbase(B)
    M1 = np.linalg.inv(M)
    res1 = M1.dot(Tcan)
    res2 = res1.dot(M)
    return res2
    
'''

def mattl(Tcan, B): #Dado [T]can e B, acha [T]B
    print(B, Tcan)
    M = np.transpose(B)
    M1 = np.linalg.inv(M)
    res1 = M1.dot(Tcan)
    res2 = res1.dot(M)
    return res2
    
'''
dado B base nao canonica
B transposta.dot(vetorB) = (vetorCan)
resolve_coef(B, VetorCan) = vetorB

'''

def poli(M): # da o polinomio caracteristico
    n = len(M)
    m2 = np.identity(n)
    m3 = np.identity(n)
    m3 = Matrix(m3)
    for i in range(n):
        for j in range(n):
            #print(m3)
            #print(i + j)
            m3[i,j] = (M[i][j] - m2[i][j] * x)
    
    return m3.det()
    
def ar(m): # lista -> array
    m = np.array(m)
                    
def vtp(vlp, M): # vetores proprios de M associados aos vlp (primeiro coef 1)
    lres = [0] * len(M)
    vtp = []
    for vl in vlp:
        m2 = M.copy()
        m2 = m2 - vl * np.identity(len(M))
        #print(m2)
        m2 = esc(m2)
        #print(m2)
        vt = t3(m2)
        vtp += [vt]
        print(f'vtp associado a vlp {vl} é {vt}')
    return vtp
            
def t3(m):
    
    
    if len(m) == 2:
        return [1, -m[0,0]/m[0,1]]
    
    #m[0] = m[0]/m[0,0]
    r = [-m[0,0]] + [0] * (len(m) - 2) 
    #print('=-==-==-')
    #print(m, r)
    mn = m[:-1, 1:]
    l = slin3(mn, r)
    l = [1] + l
    return l
def autval(m): #devolve os autovalores da matriz m
    p = poli(m)
    s = str(p) + '?'
    l = []
    num = '-0123456789'
    var = ' 0123456789.'
    maxi = len(s)
    i = 0
    #print(s)
    while i < maxi:
        letra = s[i]
        
        if (letra in num) and (s[i-1] != '*'):
            #j = i
            s0 = letra
            i += 1
            while s[i] in var:
                if s[i] != ' ': 
                    s0 = s0 + s[i]
                i += 1
            l += [s0]
            #i = j
        i+= 1
            
    #print(l)
    
    for el in range(len(l)):
        l[el] = float(l[el])
    
    l = tuple(l)
    raiz = np.roots(l)
    print(f'polinomio = {p}')
    return raiz
        
def tudo(m): # autovalores e autovetores da matriz m
    vlp = autval(m)
    print('--'* 20)
    print(f'os valores proprios de m sao {vlp}')
    print('--'* 20)
    vtpm = vtp(vlp, m)
    print('--'* 20)
    print(f'os vetores proprios de m sao {vtpm}')
    print('--'* 20)
    
def criabase(n, dim):
    base = []
    for i in range(n):
        l = [0] * dim
        l = l.copy()
        for j in range(dim):
            v = float(input(f'Digite o {j+ 1} valor da tupla {i + 1}:'))
            l[j] = v
        base += [l]
        
    ar(base)
    return base
        
def canonica(n):
    return np.identity(n)
    
def mudbase(B, C): # B ---M---> C ///  M * [u]C = [u]B
    Mt = []
    n = len(C)
    for i in range(n):
        vt = C[i].copy()
        lin = resolve_coef(B, vt)
        Mt += [lin]
    
    M = np.transpose(Mt)
    return M

def ortog(m):
    'n vetores de tamanho tam. constroi base ortogonal'
    n = len(m)
    ort = []
    ort += [m[0]]
    for i in range(1,n):
        v = m[i]
        for j in range(len(ort)):
           # print(v)
            #print(ort[j])
            #print(m[i])
            #print(  sum(m[i] * ort[j]) / sum(ort[j] * ort[j] ))
            
            w =  (  sum(m[i] * ort[j]) / sum(ort[j] * ort[j] )) * ort[j]
            #print(w)
            v = slin(v,-w)
                 
        ort += [np.array(v)]
        
    return(np.array(ort))
        
def proj(v, m):
    '''projecao do vetor v em m
    
    <v, m1> m1/ ||m1||**2 + <v, m2> m2/ ||m2||**2 (...)
    
    '''
    ar(v)
    ar(m)
    vet0 = m[0].copy()
    vet0 -= m[0]
    
    #print(f'vet 0 primeira vez = {vet0}')
    
    for i in range(len(m)):
        #print(f'v começo do for = {v}')
        
        mi = m[i].copy()
        ar(mi)
        #print(f'mi ={mi}')
        #print('mlinlin(vi, mi = ')
        #print((mlinlin(v, mi)))
        K = (sum(mlinlin(v, mi)) / sum(mlinlin(mi,mi)))
        vet = K * np.array(m[i])
        #print(f'vet = {vet}')
        #print(vet)
        
        vet0 = slin(vet0, vet)
        #print(f'vet0 = {vet0}')
        
    ar(vet0)
    return(vet0)
        
def ortog2(m):
    n = len(m)
    ort = []
    ort += [m[0]]
    for i in range(1,n):
        w =  proj(m[i], ort)
        
        #print(m[i])
        #print('w')
        #print(w)
        ar(w)
        #print(w)
        #return w
        negative_w = -1 * np.array(w)
        #print('-w')
        #print(negative_w)
        v = slin(m[i], negative_w)
        ort += [v]
    
    return(ort)
       
def pi(a, b):
    return sum(mlinlin(a,b))

def proj2(v, m):
    l = []
    for i in range(len(m)):
        mult = pi(v, m[i])
        den = pi(m[i], m[i])
        tup = (den, mult * np.array(m[i]))
        l += [tup]
        
    return l
        
def seila(u, v):
    return pi(u,v) , pi(v,v)

def orton3(m):
    ort = []
    ort += [np.array(m[0])]
    for i in range(1, len(m)):
        print()
        
def criamt(lin, col):
    l = [0] * col
    mt = []
    for i in range(lin):
        mt += [l.copy()]
    
    for i in range(lin):
       for j in range(col):
           v = float(input(f'digite o termo {j+1} da linha {i+1}: '))
           print(v)
           mt[i][j] = float(v)
            
            
    return np.array(mt)
    










m = np.array([[  0.,   0.,  -2.,   0.,   7.,  12.],
       [  2.,   4., -10.,   6.,  12.,  28.],
       [  2.,   4.,  -5.,   6.,  -5.,  -1.]])



l1 = m[2].copy()
l2 = m[1].copy()
l3 = m[0].copy()

l2 = l2 - l1
#print(l2)

l1 = l1/2
l2 = -l2/5
#print(l1)
#print(l2)
l3 = np.array([  0.,   0.,  -2.,   0.,   7.,  12.])
l3 = l3 + 2*l2
print(l3)









