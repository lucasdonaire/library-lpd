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
def indice(x, seq):
    ''' recebe um número x e uma sequencia ordenada seq
    retorna o índice entre 0 e len(seq) que x deve ser inserido para que seq continue ordenada
    '''
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
        
    return len(seq)



## ==================================================================
def main():
    '''
        Testes das suas funções

        Deve conter ao menos 10 testes distintos cobrindo casos
        básicos, como listas vazias, com apenas um elemento etc.
        e casos genéricos com vários elementos.
    '''
    print("Testes do EI22 - ordenação por intercalação")

    # escreva seus testes
    seq1, seq2 = [], []
    print('resposta ideal = [], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [1], []
    print('resposta ideal = [1], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [], [3]
    print('resposta ideal = [3], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [1,2,4], [3,5,6]
    print('resposta ideal = [1,2,3,4,5,6], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [7, 11, 56], [-5, 7, 99, 104]
    print('resposta ideal = [-5, 7, 7, 11, 56, 99, 104], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [-10, -1, 1, 10], [-5,0,5]
    print('resposta ideal = [-10,-5,-1,0,1,5,10], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [0,2,4,8,10,12,14,16,18,20], [1,3,5,7,9,11,13,15,17,19]
    print(f'resposta ideal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [1,1,1,2,3], [1,1,2,2,3,3]
    print('resposta ideal = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [1,10,100,1000], [2,20,200,2000]
    print('resposta ideal = [1,2,10,20,100,200,1000,2000], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    
    seq1, seq2 = [-100,-10,-1,1,10,100], [0]
    print('resposta ideal = [-100, -10, -1, 0, 1, 10, 100], \n resposta :', end = ' ')
    print(intercale_seqs(seq1, seq2))
    

## ------------------------------------------------------------------

def intercale_seqs(seq1, seq2):
    ''' (list, list) -> list

    Recebe seq1 e seq2, duas listas tal que:

        - seq1 é crescente com n1 >= 0 elementos e
        - seq2 é crescente com n2 >= 0 elementos
        
    Retorna uma lista com n1+n2 elementos, contendo
    os elementos de seq1 e seq2 em ordem crescente.

    Exemplo para 
        seq1 = [7, 11, 56] e 
        seq2 = [-5, 7, 99, 104]
    
    a função deve retornar a lista:
        [-5, 7, 7, 11, 56, 99, 104]
    '''

    if len(seq1) >= len(seq2):
        sg, sp = seq1.copy(), seq2.copy()
        
    else:
        sp, sg = seq1.copy(), seq2.copy()
        
    if sg == []:
        return []
    
    if sp == []:
        return sg
        
    
    for i in range(len(sp)):
        k = indice(sp[i], sg)
        sg = sg[:k] + [sp[i]] + sg[k:]
    
    return sg
            

#--------------------------------------------
if __name__ == '__main__':
    main()