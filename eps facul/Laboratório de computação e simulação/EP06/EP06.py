#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 22:14:09 2022

@author: lucasdonaire
"""

INFO = {12556552:"Lucas Panfilo Donaire",12556736:"Enzo Cappelozza"}

import numpy as np
import math
from scipy.integrate import quad
import scipy


############################################################################### criando a classe Estimador

class Estimador:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        x1,x2,x3 =  [x[0]+y[0],x[1]+y[1],x[2]+y[2]]  # vetor x+y
        self.X = [x1,x2,x3]
        num = 100000   #numero de pontos
        mean = [0,0]
        sigma = 0.02
        cov = np.array([[sigma,0],[0,sigma]]) # matriz de covariância
        ponto_inicial = (0.3,0.3)
        saltos = 10
        n_cadeia_fria = num//10
        c,taxa = self.MCMC(n_cadeia_fria,num,saltos,mean,cov,ponto_inicial)
        self.c = c
        
        
    def MCMC(self,aquecimento,tamanho_da_cadeia,saltos,mean,cov,ponto_inicial):
        #gera uma cadeia a partir do n do aquecimento, n do tamanho da cadeia e
        # tamanho dos saltos, matriz de covariancia e ponto inicial
        # funciona apenas para dimensao dois
        
        # total de pontos a serem gerados
        n = aquecimento+(tamanho_da_cadeia*saltos)
        
        # gera os valores da normal e uniforme anteriormente por vetorizacao
        normal = np.random.multivariate_normal(mean,cov,n)
        uniforme = np.random.uniform(0,1,n)
        
        #contagem dos pontos gerados para pegar o k-esimo candidato
        k = 0
        
        
        #cria a base da cadeia, apenas para facilitar o codigo
        cadeia = [0]*(tamanho_da_cadeia*saltos)
    

                            #### Aquecimento ####   
        # funcionamento igual ao topico MCMC, sem salvar a cadeia
        # Salvando apenas o ultimo membro
        cadeia_fria = ponto_inicial 
        for i in range(aquecimento):   
            atual = cadeia_fria
            proximo = (0,0)
            caminho = normal[k]
            proximo = (atual[0] + caminho[0] , atual[1] + caminho[1])
            if uniforme[k] < self.alpha(atual , proximo):
                cadeia_fria = proximo
            k += 1

        # calculo da taxa de aceitacao
        taxa_num = 0
        
                            #### MCMC ####   
        cadeia[0] = cadeia_fria        #A cadeia esquentada recebe o ultimo 
                                         #termo da fria
        for i in range((tamanho_da_cadeia*saltos)-1):     
            atual = cadeia[i]    # Posicao atual da cadeia
            # Calculo do proximo candidato
            proximo = (0,0)   
            caminho = normal[k]
            proximo = (atual[0] + caminho[0] , atual[1] + caminho[1])
                                                       # Decide se a nova posicao é
            if uniforme[k] < self.alpha(atual , proximo):    # aceita, movendo a 
                cadeia[i+1] = proximo                            # cadeia caso seja 
                taxa_num += 1 #calcula a taxa de aceitacao
            else:
                #repete o ultimo termo caso n seja aceito
                cadeia[i+1] = atual
            k += 1 
        #taxa de aceitacao
        taxa = taxa_num/len(cadeia)
            
        
        
        if saltos ==1:
            return cadeia,taxa
        
        # elimina parte da amostra para diminuir a correlacao
        cadeia_final = [0]*tamanho_da_cadeia
        for i in range(tamanho_da_cadeia):
            cadeia_final[i] = cadeia[saltos*i]
        return cadeia_final,taxa
    
    def U(self,v):
        c = self.c
        X = self.X
        x1,x2,x3 = X[0],X[1],X[2]
        soma = 0
        prod = 1
        for xi in [x1,x2,x3]:
                if xi == 0: prod*= math.gamma(0.000001)
                else: prod *= math.gamma(xi)
        q = math.gamma(x1+x2+x3)/prod
        k = v/q
        for i in c:
            if self.theta(i[0],i[1]) > k:
                soma += 1
        return 1 - (soma/len(c) )
    
    def theta(self,theta1,theta3):
        X = self.X
        x1,x2,x3 = X[0],X[1],X[2]
        # funcao potencial
        theta2 = 1 - theta1 - theta3
        if theta1 <0 or theta2<0 or theta3<0:
            return 0
        y = ((theta1**(x1-1))*(theta2**(x2-1))*(theta3**(x3-1)))
        return y
        
    
    def alpha(self,i,j):
        # alpha de aceitacao utilizado
        if self.theta(i[0],i[1]) == 0: return 1
        return self.theta(j[0],j[1])/self.theta(i[0],i[1])
          
    

############################################################################### outras funções auxiliares



def B(v): # multivariate beta function
    sv = sum(v)
    pv = 1
    for a in v:
        if a == 0: pv*= math.gamma(0.000001)
        else: pv *= math.gamma(a)
    return(pv/math.gamma(sv))

def f(x,y,theta): #posterior density function
    x,y = np.array(x),np.array(y)
    tam = len(x)
    v = x+y
    v1 = v-1
    q = B(v)
    p = 1
    for i in range(tam):
        p *= theta[i]**v1[i]
    return p/q

def fpotential(x,y,theta): #função potencial da densidade
    x,y = np.array(x),np.array(y)
    tam = len(theta)
    v = x+y-1
    p = 1
    for i in range(tam):
        p *= theta[i]**v[i]
    return p


def minus_fpot(x, y, t_1): # -f, com theta seguindo as restrições de H
    t_3 = (1-math.sqrt(t_1))**2
    t_2 = (1 - t_1 - t_3)
    theta = (t_1, t_2, t_3)
    return -fpotential(x,y,theta)
    
def findargmax(x,y):
    #achar theta na hipotese que maximiza fpotencial(x,y,theta)
    
    pt = scipy.optimize.minimize_scalar(lambda t_1: minus_fpot(x,y,t_1), bounds = (0,1), method='bounded')
    
    t_1f = pt.x
    t_3f = (1-math.sqrt(t_1f))**2
    t_2f = (1- (t_1f + t_3f))
    
    
    return ([t_1f, t_2f, t_3f])




def integrand_gamma(x, k):
    return x**(k-1) * np.exp(-x)

def Gamma(k,z): # funcao gamma de dois argumentos, como definido no video do ep6
    I = quad(integrand_gamma, 0, z, args=(k))
    return I[0]


def QQ(t,h,z): # funcao QQ, como definido no video do ep6
    return Chi2(t-h,1/Chi2(t,z))

def Chi2(k,z): # funcao Chi2, como definido no video do ep6
    return Gamma(k/2,z/2)/math.gamma(k/2) # math.gamma(x) = Gamma(x, infinity)



###############################################################################
# printando os resultados para os X, Y adequados

t=2
h=1
xs = [[1, 17, 2], [1, 16, 3], [1, 15, 4], [1, 14, 5], [1, 13, 6], [1, 12, 7], 
      [1, 11, 8], [1, 10, 9], [1, 9, 10], [1, 8, 11], [1, 7, 12], [1, 6, 13], 
      [1, 5, 14], [1, 4, 15], [1, 3, 16], [1, 2, 17], [1, 1, 18], [5, 15, 0], 
      [5, 14, 1], [5, 13, 2], [5, 12, 3], [5, 11, 4], [5, 10, 5], [5, 9, 6], 
      [5, 8, 7], [5, 7, 8], [5, 6, 9], [5, 5, 10], [9, 11, 0], [9, 10, 1], 
      [9, 9, 2], [9, 8, 3], [9, 7, 4], [9, 6, 5], [9, 5, 6], [9, 4, 7]]

ys = [[1,1,1],[0,0,0]]

for x in xs:
    for y in ys:
        thetastar = findargmax(x,y)
        sstar = f(x,y,thetastar)
        estimador = Estimador(x, y)
        ev = estimador.U(sstar)
        evbar = max(1-ev,0.0001)
        sev = 1 - QQ(t,h,evbar)
        H = sev >= 0.05
        print(f"x1={x[0]}, x3={x[2]}, Y= {y[0]}, H={H},  θ*= {thetastar}, ev(H|X)={ev} e sev(H|X)={sev}")



