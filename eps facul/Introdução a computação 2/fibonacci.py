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
def main():
    from timeit import default_timer as timer
    l = [10, 20, 30, 40, 50]
    ti = []
    tr = []
    for it in l:
        t0 = timer()
        fibR = fibonacciR(it)
        t1 = timer()
        fibI = fibonacciI(it)
        t2 = timer()
        ti += [t2 - t1]
        tr += [t1 - t0]
    print('--i--')
    print(ti)
    print('--r--')
    print(tr)
        
    
    '''
    resultado
  Iterativo
[4.551999154500663e-06, 
 4.012999852420762e-06, 
 1.0245999874314293e-05, 
 7.262999133672565e-06, 
 0.6569330189995526]

  Recursivo
[3.850799839710817e-05, 
 0.0038008400006219745, 
 0.500223647999519, 
 59.65714235199994, 
 7959.116024216]
    '''


## ==================================================================

def fibonacciR(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma recursiva.
    Retorna o valor calculado.

    Exemplos:
    fibonacciR(5) = 5
    fibonacciR(10) = 55
    fibonacciR(20) = 6765
    fibonacciR(30) = 832040
    fibonacciR(40) = 102334155
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)
    

## ==================================================================

def fibonacciI(n):
    '''(int) -> int

    Recebe um inteiro não negativos n e calcula o
    n-ésimo número de fibonacci de forma iterativa.
    Retorna o valor calculado.
    '''
    
    n1 = 1
    na = 0
    for i in range(n):
        na, n1 = na + n1, na
    return na
        




if __name__ == '__main__':
    main()
    

    
    
    
    
    
    
    
    
    
