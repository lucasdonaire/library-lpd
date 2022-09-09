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

import random

## ==================================================================
#     Constantes que você pode usar em sua solução

DATAS = 365
SUCESSO = True
FRACASSO = False

## ==================================================================
# 
def main():
    '''
    Testes da classe Aniversario

    inclua mais 10 testes usando valores distintos de n e t.
    '''

    print("Testes do EI27 - Paradoxo do Aniversário")
    n = 1
    t = 1000
    print(Aniversario(n, t))
    
    n = 10
    t = 1
    print(Aniversario(n, t))
    
    n = 10
    t = 10
    print(Aniversario(n, t))
    
    n = 10
    t = 100
    print(Aniversario(n, t))
    
    n = 10
    t = 1000
    print(Aniversario(n, t))
    
    n = 10
    t = 10000
    print(Aniversario(n, t))
    
    n = 50
    t = 1000
    print(Aniversario(n, t))
    
    n = 100
    t = 50000
    print(Aniversario(n, t))
    
    n = 365
    t = 50000
    print(Aniversario(n, t))
    
    n = 400
    t = 10000
    print(Aniversario(n, t))
    


## ==================================================================
# 
class Aniversario:

    #------------------------------------------
    def __init__(self, n, t):
        '''(Aniversario, int, int) -> None

        Recebe o número n de pessoas que podem entrar na sala
        e o número t de experimentos (trials). 
        Calcula a probabilidade de, ao selecionarmos n 
        datas uniformemente ao acaso, tenhamos
        duas datas iguais.
        '''        
        self.n = n
        self.t = t
        sucessos = 0
        for i in range(t):
            sucessos += self.experimento()
        self.p = sucessos/t    

    #------------------------------------------    
    def __str__(self):
        return str(self.p)

    #------------------------------------------    
    def mean(self):
        return self.p

    #-----------------------------------------
    def experimento(self):
        ''' (Aniversario) -> bool

        Executa um experimento como descrito no enunciado,
        para uma sala com até 
        * self.n pessoas e 
        * self.t tentativas (trials)
        Retorna SUCESSO ou FRACASSO.

        DICA: para esse método, conjuntos são mais 
        eficientes que listas.
        '''

        # implemente sua solução
        n = self.n
        l = []
        dias = list(range(1, 366))
        for i in range(n):
            sorteio = random.choice(dias)
            if sorteio in l:
                return True
            l += [sorteio]
        
        return False

## ==================================================================
# 
if __name__ == '__main__':
    main()