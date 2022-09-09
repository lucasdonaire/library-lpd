# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Lucas Panfilo Donaire
    NUSP: 12556552

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que trabalhos sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    
    Estou ciente que os casos de plágio e desonestidade acadêmica
    estarão sujeitos às penalidades descritas na página da disciplina
    na seção "Sobre colaboração em MAC0122".

    Reconheço que utilizei as seguintes fontes externas ao conteúdo 
    utilizado e recomendado em MAC0122, ou recebi auxílio das pessoas
    listadas abaixo.

    - LISTA de fontes externas utilizadas (links ou referências como livros)
        - 

    - LISTA das pessoas que me auxiliaram a fazer esse trabalho
        - 
'''

import numpy as np

## CONSTANTES

DEBUG = True

## ==================================================================

def binomialI(n, k):
    '''(int, int) -> int
    RECEBE dois inteiros não negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialI(3,2)  -> deve retornar 3
    b) binomialI(5,1)  -> deve retornar 5
    c) binomialI(1,5)  -> deve retornar 0
    d) binomialI(4,2)  -> deve retornar 6

    NOTA. Está função é iterativa.
    '''
    if n == k: return 1
    if k > n : return 0
    if k == 0: return 1
    mat = np.identity(max(n,k) + 1)
    mat[:,0] = [1]
    
    ni = 2
    #ki = 1
    while mat[n,k] == 0:
        ki = 1
        while ki < ni:
            mat[ni, ki] = mat[ni-1, ki-1] + mat[ni-1, ki]
            ki += 1
        ni += 1
        
    return mat[n,k]
            
        
        
        
    

## ==================================================================

def binomialR(n, k):
    '''(int,int) -> int

    RECEBE inteiros não-negativos n e k.
    RETORNA o valor de binomial(n,k).

    Exemplos:
    a) binomialR(3,2)  -> deve retornar 3
    b) binomialR(5,1)  -> deve retornar 5
    c) binomialR(1,5)  -> deve retornar 0
    d) binomialR(4,2)  -> deve retornar 6

    NOTA. Está função é uma interface para a função 
          binomialRM() e não deve ser alterada.
    '''
    # cria um array de dimensão (n+1)x(k+1) para ser usado como rascunho
    rascunho = np.zeros((n+1, k+1), int) 
    rascunho[:,0] = 1

    bin = binomialRM(n, k, rascunho)
    if DEBUG:
        print("Debug ligado.")
        print(f"bin({n}, {k}) = {bin}")
        print(f"   Rascunho:\n{rascunho}")

    return bin

## ==================================================================

def binomialRM(n, k, rascunho):
    '''(int, int, array) -> int

    RECEBE inteiros não negativos n e k e um array bidimensional rascunho.
    RETORNA o valor de binomial(n,k).

    NOTA. Está função é recursiva.
        Ela usa as posições do array rascunho para  guardar os valores dos 
        binomiais já calculado: 
           - rascunho[i][j] armazenará o valor de binomial(i, j).
        Com isso a função evita que um mesmo número binomial seja recalculado 
        várias vezes.
    '''
    if n == k: 
        rascunho[n, k] = 1
        return 1
    if k > n :
        rascunho[n, k] = 0
        return 0
    if k == 0: 
        rascunho[n, k] = 1
        return 1
    
    if rascunho[n-1,k-1] == 0:
        rascunho[n-1,k-1] = binomialRM(n-1, k-1, rascunho)
    if rascunho[n-1, k] == 0:
        binomialRM(n-1, k, rascunho)
        
    rascunho[n,k] = rascunho[n-1,k-1] + rascunho[n-1,k]
    
    return rascunho[n,k]
         
    
        
    
    
    
    
    
    
    

