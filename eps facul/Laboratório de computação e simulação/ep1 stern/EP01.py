#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
#Escreva seu nome e numero USP
INFO = {12556552:"Lucas Panfilo Donaire"}
import numpy as np
def estima_pi(Seed = None):

    random.seed(Seed)
    #random.random() gera um numero com distribuicao uniforme em (0,1)
    """
    Esta funcao deve retornar a sua estimativa para o valor de PI
    Escreva o seu codigo nas proximas linhas
    """
    np.random.seed(Seed)    
    n = 90000000 #15366400
    x = np.random.uniform(0,1,n) # array de tamanho n de U[0,1]
    y = np.random.uniform(0,1,n) # array de tamanho n de U[0,1]
    cont = np.sum(x**2 + y**2 <= 1) # soma 1 para cada ponto que está contido no círculo unitário
    # se [sqrt(x**2 + y**2) <= 1] então [x**2 + y**2 <= 1]
    return 4*cont/n  # /n = aproximadamente pi/4 -> pi = 4*cont/n



print(estima_pi())