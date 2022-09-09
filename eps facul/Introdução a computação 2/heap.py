# -*- coding: utf-8 -*-

#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
#------------------------------------------------------------------

'''

    Nome: Lucas Panfilo Doanire
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

    print("Testes do EI24 - ordenação usando max heap")

    x = [21, 12, 43, 61, 41, 71, 91, 31, 81]
    print(f"Entrada:\n{x}")

    print("\n testes do insira")

    h = MaxHeap()
    for item in x:
        h.insira(item)
        print(h)
        input("Tecle enter para continuar ...")

    print("\n teste do construa")
    h = MaxHeap()
    h.construa(x)
    print(h)

## ==================================================================

class MaxHeap:

    def __init__(self):
        ''' (MaxHeap) -> None
        Construtor da classe MaxHeap.
        Cria uma lista self.data com [None].
        '''
        self.data = [None]

    def __len__(self):
        ''' (MaxHeap) -> int
        Retorna o número de elementos no heap.
        O elemento no índice zero não faz parte do heap.
        '''

        return len(self.data) - 1

    def __str__(self):
        ''' (MaxHeap) -> str
        Retorna uma representação texto do heap.
        '''

        n = len(self.data)
        dt = self.data

        nivel = 0
        txt = '\n'

        i = 1
        while i < n:
            fim = 2 ** nivel
            nivel += 1
            filho = 0
            while i < n and filho < fim:
                txt += f'{dt[i]}\t'
                i += 1
                filho += 1
            txt += '\n'
        return txt

    def insira(self, item):
        ''' (MaxHeap, obj) -> None
        Recebe um número obj e o insere no heap.

        Inicialmente, o item deve ser colocado no final da lista. 
        Em seguida, enquanto o pai desse item for menor, o item
        deve subir na árvore até sua posição correta. 

        Exemplo:
        Caso self.data seja a lista [None], a inserção de 21 deve
        rearranjar self.data para que se torne: [None, 21].

        Caso self.data seja a lista [None, 21], a inserção de 12 deve
        rearranjar self.data para que se torne: [None, 21, 12].
        
        Caso self.data seja a lista [None, 21, 12] a inserção de 43 
        deve rearranjar self.data para que se torne: [None, 43, 12, 21].

        Caso self.data seja a lista [None, 43, 12, 21] a inserção de 65
        deve rearranjar self.data para que se torne: [None, 65, 43, 21, 12].

        Dica: desenhe as árvores binárias correspondentes.

        '''

        # escreva sua solução
        self.data.append(item)
        ind1 = len(self.data) - 1
        while ind1 != 1:
            ind2 = ind1 // 2
            if self.data[ind2] >= self.data[ind1]:
                return
            self.data[ind2], self.data[ind1] = self.data[ind1], self.data[ind2]
            ind1 = ind2 
            


    def construa(self, seq):
        ''' (MaxHeap, list) -> None
        Recebe uma lista de números seq. 
        Para cada item em seq, insere o item no heap
        usando o método insira. Dessa forma, seq é
        transformada em um max heap em self.data.
        '''

        # escreva sua solução
        for item in seq:
            self.insira(item)



if __name__ == '__main__':
    main()