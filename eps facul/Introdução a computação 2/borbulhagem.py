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

## ==================================================================

def main():
    '''
        Testes das suas funções
    '''
    print("Testes do EI21 - ordenação por borbulhagem")


def borbulhe(seq, n):
    ''' (list, int) -> int

    RECEBE uma lista seq e um inteiro n.

    A função deve PERCORRER sequencialmente a lista seq. O percurso 
    deve ser da posição de índice 0 até a posição de índice n. 

    Durante o percurso a função COMPARA todos os pares de valores 
    em posições vizinhas, como por exemplo seq[0] e seq[1], seq[5] 
    e seq[6] e em geral seq[i] e seq[i-1] para todo i, 0 < i < n.

    Se os valores comparados não estiverem em ordem crescente, eles devem ser
    TROCADOS de posições. Por exemplo, para 

        seq = [w, x, y, 7, 5, z] 

    a comparação de seq[3]=7 e seq[4]=5 deve resultar na troca de seus valores. 
    A lista deve ser modificada de tal forma que tenhamos  
   
        seq = [w, x, y, 5, 7, z], 

    em que os valores w, x, y e z são irrelevantes.

    RETORNA o número de trocas realizadas durante o percurso.

    Esta função será o coração de mais um algoritmo de ordenação que nos 
    apresentará novas ideias.

    EXEMPLOS:

    In [24]: seq = [7, 4, 11, 5, 3]
    In [25]: t = borbulhe(seq, 3)
    In [26]: t
    Out[26]: 1
    In [27]: seq
    Out[27]: [4, 7, 11, 5, 3]

    In [28]: seq = [7, 4, 11, 5, 3]
    In [29]: t = borbulhe(seq, 4)
    In [30]: t
    Out[30]: 2
    In [31]: seq
    Out[31]: [4, 7, 5, 11, 3]

    In [32]: seq = [7, 4, 11, 5, 3]
    In [33]: t = borbulhe(seq, 5)
    In [34]: t
    Out[34]: 3
    In [35]: seq
    Out[35]: [4, 7, 5, 3, 11]

    SUGESTÃO: não use listas auxiliares como fatias. Basta
    percorrer seq, comparar pares vizinhos e trocar quando
    necessário.
    '''
    cont = 0
    for i in range(1,n):
        if seq[i-1] > seq[i]:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            cont += 1
            
    return cont
            
        
        

## ==================================================================

def ordene_por_borbulhagem(seq):
    ''' (list) -> int

    RECEBE uma lista seq e REARRANJA seus elementos de tal forma que
    fiquem ordenados.

    Esta função DEVE APLICAR repetidas vezes a função borbulhe() sobre a 
    lista seq até que seq esteja ordenada. 

    RETORNA o número total de trocas realizadas durante a ordenação. 

    Cada vez que a função borbulhe() é aplicada sobre a lista seq, os elementos
    da lista ficam mais próximos de seus lugares na lista ordenada.

    EXEMPLO. Suponha que seq = [7, 4, 11, 5, 3]. 
    Após aplicarmos borbulhe() sobre a lista seq na
 
        * primeira vez, obtemos seq=[4, 7, 5, 3, 11], com  3 trocas
        * segunda  vez, obtemos seq=[4, 5, 3, 7, 11], mais 2 trocas
        * terceira vez, obtemos seq=[4, 3, 5, 7, 11], mais 1 troca
        * quarta   vez, obtemos seq=[3, 4, 5, 7, 11], mais 1 troca

    Pronto! A lista seq está ordenada.
    Para seq = [7, 4, 11, 5, 3] a função deve retornar 7.
    '''
    t = 1
    cont = 0
    while t != 0:
        t = borbulhe(seq, len(seq))
        cont += t
        
    return cont

## ==================================================================    
if __name__ == '__main__':
    main()
