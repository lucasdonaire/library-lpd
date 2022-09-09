#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random

#Escreva seu nome e numero USP
INFO = {12556552:"Lucas Panfilo Donaire"}
A = 0.57892819  # A = 0.rg
B = 0.47410024895  # B = 0.cpf


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
    n = 7160371
    x = np.random.uniform(0,1,n) 
    fx = f(x)
    mean = sum(fx)/n # média
    return mean




def hit_or_miss(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo hit or miss
    Escreva o seu codigo nas proximas linhas
    """
    n = 7160371
    x = np.random.uniform(0,1,n)
    y = np.random.uniform(0,1,n)
    fx = f(x)
    return sum(y < fx)/n # quantos pontos estão abaixos de f(x)



def control_variate(Seed = None):
    random.seed(Seed)
    """
    Esta funcao deve retornar a sua estimativa para o valor da integral de f(x)
    usando o metodo control variate
    Escreva o seu codigo nas proximas linhas
    """
    def h(x): return 1 - 0.5*x # nossa h(x)
    inth = 0.75 # integral de h(x)
    n = 1195404
    x = np.random.uniform(0,1,n)
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
    n = 7160371
    u = np.random.uniform(0,1,n)
    x = invG(u)
    fx = f(x)
    gx = g(x)
    return sum(fx/gx)/n


def main():
    #Coloque seus testes aqui
    print(crude())
    print(hit_or_miss())
    print(control_variate())
    print(importance_sampling())
    



if __name__ == "___main__":
    main()