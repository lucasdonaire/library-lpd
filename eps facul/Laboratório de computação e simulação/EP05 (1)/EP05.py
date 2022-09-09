#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Escreva seus nomes e numeros USP
INFO = {12556552:"Lucas Panfilo Donaire",12556736:"Enzo Cappelozza"}

import numpy as np
import math
import random
from scipy import stats

##################################################

def fpotential(x,y,theta):
    x,y = np.array(x),np.array(y)
    tam = len(theta)
    v = x+y-1
    p = 1
    for i in range(tam):
        p *= theta[i]**v[i]
    return p


def warmUp(f, geray): # 'aquecer' a cadeia de markov antes de usar os pontos de fato
    p0 = np.array([0.1,0.1,0.8])
    for i in range(100):
        p = p0 + geray()
        k = f(p)/f(p0)
        alf = min(1,k)
        u = random.uniform(0,1)
        if u <= alf and f(p) > 0:
          p0 = p
    return p0
    
def mcmc(f,geray,n): # gerar n lista de pontos com distribuicao f, tal que t_i+1 = t_i + y, e y~geray
    l =[]
    p0 = warmUp(f,geray)
    l.append(p0)
    while len(l) < n:
        p = p0 + geray()
        k = f(p)/f(p0)
        alf = min(1,k)
        u = random.uniform(0,1)
        if u <= alf:
          l.append(p)
          p0 = p
    return l
    

def geray(sigma=np.eye(2),mean=[0,0]): # estamos gerando y com duas normais N(0,3/10)
    N = multNormal(0.3*sigma,mean)
    nv = N.rvs(1)
    y0 = np.array([nv[0], nv[1], -nv[0]-nv[1]])
    return y0


def multNormal(sigma = np.eye(3), mean = [0,0,0]): #obj para gerar uma normal multivariada media mean, matriz de cov sigma
    N = stats.multivariate_normal(mean=mean,cov=sigma)
    return N



def gerador_mcmc(x,y,n): # gera theta~f por MCMC
    def f(theta):
        theta = np.array(theta)
        if not np.allclose(sum(theta),1): return 0
        if len(theta[theta>0]) != 3: return 0
        return fpotential(x,y,theta)

    return mcmc(f,geray,int(n))




##################################################
def amostra_MCMC(x,y,n):
    """
    Funcao que recebe valores pros vetores x e y, o tamanho n da amostra, 
    gera uma amostra de tamanho n a partir do metodo de monte carlo via 
    cadeias de markov, onde cada elemento da amostra tem tamanho 3 (vetor),
    e retorna uma lista de tamanho n com os potenciais de cada ponto obtido,
    onde cada elemento tem tamanho 1 (escalar).
    
    Nao utilize a fuancao densidade de probabilidade, apenas a funcao potencial!
    """
    amostra_de_potenciais = []
    theta = gerador_mcmc(x,y,n)
    for t in theta:
        amostra_de_potenciais.append(fpotential(x, y, t))        

    return amostra_de_potenciais # Exemplo do formato = [0.04867, 0.00236, 0.00014 ... ]



    
class Estimador:
    """
    Classe para criar o objeto, ele recebe valores para os vetores x e y.
    Os metodos definidos abaixo serao utilizadas por um corretor automatico. Portanto,
    precisa manter os outputs e inputs dos 2 metodos abaixo. 
    """
    def __init__(self,x,y):
        """
        Inicializador do objeto. Este metodo recebe 
        valores pros vetores x e y em formato de lista 
        e implementa no objeto. 
        """
        self.vetor_x = x #formato: [0,0,0] - List cujo len(x) = 3
        self.vetor_y = y #formato: [0,0,0] - List cujo len(y) = 3
        #Continue o codigo conforme achar necessario.
        a = []
        for i in range(len(x)): 
          a.append(x[i] + y[i])
        self.a = np.array(a)
        self.q = self.B(self.a)


        n = 15000 

        
        fvalues = amostra_MCMC(x, y, n) ####
        self.bins = 15000 
        LF = [0]
    
        for i in range(self.bins):
            LF.append(fvalues[n//self.bins*i])
        LF.append(fvalues[-1])
        
        self.LF = sorted(set(LF))

    def f(self,theta):
        '''
        posterior density function
        '''
        tam = len(theta)
        p = 1
        for i in range(tam):
            p *= theta[i]**(self.a[i]-1)
        return p/self.q
    
    def B(self,a): # multivariate beta function
        '''
        '''
        soma = math.gamma(self.a.sum())
        prod = 1
        for i in range(3):
            prod *= math.gamma(self.a[i])
            
        return prod/soma

        
    def U(self,v):
        """
        Este metodo recebe um valor para v e, a partir dele, retorna U(v|x,y) a partir dos 
        vetores x e y inicializados anteriormente
        """
        # Continue o codigo conforme achar necessario
        v0 = v * self.q
        if v0 < min(self.LF): u=0
        elif v0 > max(self.LF): u=1
        else:
            sv = np.array(self.LF)
            u = len(sv[sv<=v0])/len(sv)
                

  #      u = f"--'Coloque aqui a sua estimativa para U({v}|x,y)'--" 
        return u
        
    
    
def main():
    #Coloque seus testes aqui
    print("Segue um exemplo de funcionamento:")
    print("Criando o objeto")
    estimativa = Estimador([0,0,0],[0,0,0,0])
    print("Implementando o valor para v")
    print(f"Temos que U({42}) = {estimativa.U(42)}")
    print(f"Para um novo valor de v, temos que U({5/4}) = {estimativa.U(5/4)}")
    print()
    print(f"Os valores dos vetores utilizados sao: {estimativa.vetor_x,estimativa.vetor_y}")
    print("Este exemmplo foi feito para demonstrar o funcionamento esperado do objeto")




if __name__ == "__main__":
    main()
    
    
