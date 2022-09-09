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

## ==================================================================

def busca_sequencial( seq, item ):
    ''' (obj, lista) -> int ou None

        Recebe uma lista seq e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        Caso obj não esteja na lista, então a função retorna None.

        OBS: esse é um exercício muito simples para que possamos
        ver a diferença desse algoritmo com os demais. Por isso,
        não use o método index.

        Pré condição: a lista seq não está ordenada.

        Exemplos:

        para seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6] então:

        > busca_sequencial( seq, 0) retorna 5
        > busca_sequencial( seq, 8) retorna 2
        > busca_sequencial( seq, -1) retorna None

    '''
    # escreva sua solução
    for i in range(len(seq)):
        if seq[i] == item:
            return i
        
    return None
            

## ==================================================================

def busca_sequencial_em_lista_ordenada( seq, item ):
    ''' (lista, obj) -> int ou None

        Recebe uma lista seq em ordem crescente e um elemento obj. 
        Caso obj esteja na lista, devolve o índice da ocorrência de 
        obj em seq. Você pode assumir que todos os itens são
        diferentes.
        
        Caso obj não esteja na lista, então a função retorna None.

        Observe que dependendo do sentido da varredura da lista 
        ordenada, só é necessário percorrer enquanto os itens 
        forem maiores ou menores que o obj.

        Pré condição: a lista seq está ordenada em ordem crescente.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_sequencial_em_lista_ordenada( seq, 0) retorna None
        > busca_sequencial_em_lista_ordenada( seq, 8) retorna 6
        > busca_sequencial_em_lista_ordenada( seq, -1) retorna None

    '''
    # escreva sua solução
    for i in range(len(seq)):
        if seq[i] == item:
            return i
        if seq[i] > item:
            return None
    
    return None

## ==================================================================

def busca_binariaR( seq, item ):
    ''' (lista, obj) -> int ou None

        interface para a busca binária recursiva com esq e dir.
        Esq e dir indicam os índices da porção da lista onde 
        item deve ser procurado.

        Exemplos:

        para seq = [2, 3, 4, 5, 6, 7, 8, 9] então

        > busca_binariaR( seq, 0) retorna None
        > busca_binariaR( seq, 8) retorna 6
        > busca_binariaR( seq, -1) retorna None

        Não modifique essa função.
    '''

    esq = 0
    dire = len(seq)
    return busca_binariaRED(seq, item, esq, dire)

## ==================================================================

def busca_binariaRED( seq, item, esq, dire ):
    ''' (lista, obj, int, int) -> int ou None

        A ideia de busca binária em sequencia ordenada é testar o meio
        da porção da lista delimitada por [esq : dir].

        Implemente a seguinte ideia recursiva:
        - Se o intervalo for nulo, retorna None. 
        
        - Se o item de seq no meio do intervalo for o elemento procurado, 
        retorna esse índice do meio. 
        
        - Caso contrário, se o meio for maior que o procurado, então
        a busca deve continuar recursivamente na metade menor dada por [esq:meio].
        
        - Caso contrário, a busca deve continuar na outra metade (maior) do
        intervalo.

    '''
    # escreva sua solução
    if esq > dire:
        return None
    
    med = int((esq+dire)/2)
    if seq[med] == item:
        return med
    
    if esq == dire:
        return None
    
    if seq[med] > item:
        return busca_binariaRED(seq, item, esq, med)
    
    else:
        return busca_binariaRED(seq, item, med, dire)
        
    
    

## ==================================================================
## Coloque aqui outras funções que desejar


def main():
    seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6]

    print('TESTES DE busca_sequencial')    
    print(f'Quando seq = [4, 7, 8, 3, 2, 0, 1, 5, 9, 6]\n')
    print(f'Se chamado busca_sequencial para o valor 0 o return é {busca_sequencial( seq, 0)}')
    print(f'Se chamado busca_sequencial para o valor 8 o return é {busca_sequencial( seq, 8)}')
    print(f'Se chamado busca_sequencial para o valor -1 o return é {busca_sequencial( seq, -1)}')
    
    print('\n\nTESTES DE busca_sequencial_em_lista_ordenada')  
    seq = [2, 3, 4, 5, 6, 7, 8, 9]
    print(f'Quando seq = [2, 3, 4, 5, 6, 7, 8, 9]\n')
    print(f'Se chamado busca_sequencial_em_lista_ordenada para o valor 6.5 o return é {busca_sequencial_em_lista_ordenada( seq, 6.5)}')
    print(f'Se chamado busca_sequencial_em_lista_ordenada para o valor 8 o return é {busca_sequencial_em_lista_ordenada( seq, 8)}')
    print(f'Se chamado busca_sequencial_em_lista_ordenada para o valor -1 o return é {busca_sequencial_em_lista_ordenada( seq, -1)}')
    print(f'Se chamado busca_sequencial_em_lista_ordenada para o valor 9 o return é {busca_sequencial_em_lista_ordenada( seq, 9)}')
    print(f'Se chamado busca_sequencial_em_lista_ordenada para o valor 2 o return é {busca_sequencial_em_lista_ordenada( seq, 2)}')

   
    print('\n\nTESTES DE busca_binariaRED')  
    seqb = [2, 3, 4, 5, 6, 7, 8, 9, 14, 16, 24, 56, 122]
    print(f'Quando seqb = [2, 3, 4, 5, 6, 7, 8, 9, 14, 16, 24, 56, 122]')
    print('posiçoes       0  1  2  3  4  5  6  7  8   9   10  11  12\n')
    print(f'Se chamado busca_binariaR para o valor 0 o return é {busca_binariaR( seqb, 0)}')
    print(f'Se chamado busca_binariaR para o valor 8 o return é {busca_binariaR( seqb, 8)}')
    print(f'Se chamado busca_binariaR para o valor -1 o return é {busca_binariaR( seqb, -1)}')
    print(f'Se chamado busca_binariaR para o valor 24 o return é {busca_binariaR( seqb, 24)}')
    print(f'Se chamado busca_binariaR para o valor 122 o return é {busca_binariaR( seqb, 122)}')
    print(f'Se chamado busca_binariaR para o valor 14 o return é {busca_binariaR( seqb, 14)}')
    print(f'Se chamado busca_binariaR para o valor 2 o return é {busca_binariaR( seqb, 2)}')


if __name__ == '__main__':
    main()