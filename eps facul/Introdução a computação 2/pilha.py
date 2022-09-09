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
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' str --> bool
    recebe uma string e retorna True se ela for um palindromo, e False caso contrário
    usa a classe Pilha para isso
    '''
    p1 = Pilha()
    p1c = Pilha()
    p2 = Pilha()
    
    for letra in s:
        p1.empilhe(letra)
        p1c.empilhe(letra)
        
    for letra in s:
        l = p1c.desempilhe()
        p2.empilhe(l)
        
    return p1 ==p2
        
        
    


    


## ==================================================================
##
class Pilha:

    def __init__(self):
        self.dados = []
        
    def vazia(self):
        return self.dados == []

    def empilhe(self, item):
        self.dados += [item]
        
    def topo(self):
        return self.dados[-1]
    
    def __len__(self):
        return len(self.dados)
    
    def desempilhe(self):
        x = self.dados[-1]
        self.dados = self.dados[:-1]
        return x

    def __eq__(self, other):
        return self.dados == other.dados
## ==================================================================
## Escreva outras funções e classes caso desejar
def testes():

    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")

## ==================================================================
if __name__ == '__main__':
    palindromo( '' )