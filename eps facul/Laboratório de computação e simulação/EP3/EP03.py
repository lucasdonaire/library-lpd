#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random
import time

#Escreva seu nome e numero USP
INFO = {12556552:"Lucas Panfilo Donaire"}
A = 0.57892819  # A = 0.rg
B = 0.47410024895  # B = 0.cpf



def halton(b, tam):
    """Generator function for Halton sequence in [0,1]."""
    n, d = 0, 1
    l = []
    for i in range(tam):
        x = d - n
        if x == 1:
            n = 1
            d *= b
        else:
            y = d // b
            while x <= y:
                y //= b
            n = (b + 1) * y - x
        l += [n / d]
    return l
    


def f(x):
    """
    Esta funcao deve receber x e devolver f(x), como especifcado no enunciado
    Escreva o seu codigo nas proximas linhas
    """
    return np.exp(-A*x)*np.cos(B*x)




def crude(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo crude
    Escreva o seu codigo nas proximas linhas
    """
    n = 50000
    x = np.array(halton(2,n))
    fx = f(x)
    meanf = sum(fx)/n # média
    return meanf






def hit_or_miss(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """
    n = 90000
    x = np.array(halton(2,n))
    y = np.array(halton(3,n))
    fx = f(x)
    return sum(y < fx)/n 






def control_variate(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """
    def h(x): return 1 - 0.5*x # nossa h(x)
    inth = 0.75 # integral de h(x)
    n = 400
    x = np.array(halton(2,n))
    fx = f(x)
    hx = h(x)
    result = sum(fx-hx)/n + inth
    return result




def importance_sampling(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo importance sampling
    Escreva o seu codigo nas proximas linhas
    """
    def g(x): return (4 - 2*x)/3 # g escolhida, proporcional a f
    def invG(u): return (4 - np.sqrt(16-12*u))/2 # inversa generalizada de G, tal que G é a acumulada de g
    n = 800
    u = np.array(halton(2,n))
    x = invG(u)
    fx = f(x)
    gx = g(x)
    return sum(fx/gx)/n





#######
def mean(l):
  return sum(l)/len(l)


def erro(l_est): # teste de erro de uma lista de estimativas
  inf = 0.7349978686368964   
  sup = 0.73499787030797
  max_v = sup * 1.0005
  min_v = inf * 0.9995
  l_est = np.array(l_est)
  ln = []
  p = 0
  for i in range(len(l_est)):
    if max_v >= l_est[i] >= min_v:
      p += 1

    if l_est[i] > sup:
      e = abs((l_est[i] - sup)/sup)
      ln += [e]
    elif l_est[i] < inf:
      e = abs((l_est[i] - inf)/inf)
      ln += [e]
    else:
      ln += [0] # estimativa contida em [inf, sup]
  ln = np.array(ln)
  l = [mean(ln), p/len(l_est)]
  return l


def primos(): # gerador de números primos
  p = []
  a = 1
  while True:
    a += 1
    pr = True
    for primo in p:
      if a%primo == 0:
        pr = False
        #break
    if pr:
      p += [a]
      yield a
      
      
def rodar_halton(f,np,nv): # testar a função f com np pontos para os nv primeiros primos
  res = []
  s = primos()
  lp = list(next(s) for _ in range(nv))
  if f == hit_or_miss:
    for i in range(len(lp)-1):
      b1 = 2
      b2 = lp[i+1]
      res += [f(np,b1,b2)]
  else:
    for p in lp:
      res += [f(np,p)]
  return erro(np.array(res))
########

def teste_tempo():
    inicio = time.time()
    print('crude')
    e = crude()
    fim = time.time()
    print(fim - inicio)
    print('---')
    
    inicio = time.time()
    print('hit or miss')
    e = hit_or_miss()
    fim = time.time()
    print(fim - inicio)
    print('---')
    
    inicio = time.time()
    print('control variate')
    e = control_variate()
    fim = time.time()
    print(fim - inicio)
    print('---')
    
    inicio = time.time()
    print('importance sampling')
    e = importance_sampling()
    fim = time.time()
    print(fim - inicio)


def main():
    #Coloque seus testes aqui
    print(crude())
    print(hit_or_miss())
    print(control_variate())
    print(importance_sampling())
    
    e1 = crude()
    e2 = hit_or_miss()
    e3 = control_variate()
    e4 = importance_sampling()
    print()
    print(erro([e1,e2,e3,e4]))
    print()
    print('teste de tempo')
    teste_tempo()
    




if __name__ == "__main__":
    main()