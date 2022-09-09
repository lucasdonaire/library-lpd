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


import numpy as np

## ------------------------------------------------------------------
def main():

    print("Testes da classe NPImagem\n")
    lista = list(range(20))
    ar = np.array(lista).reshape(4,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1,2] = -10
    print(f"img2[1,2]={img2[1,2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop() ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)  
    print(f"img4:\n{img4}\n")

    img5 = NPImagem( (3,2) )
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1,2)
    print(f"img6:\n{img6}\n")

## ------------------------------------------------------------------
class NPImagem:
    
    def __init__(self, shape, val=0):
        if type(val) == np.ndarray:
            self.data = val
            self.shape = val.shape
        else:
            self.data = np.full(shape, val)
            self.shape = shape
        
    def __str__(self):
        s = str(self.data)
        return s
    
    def __getitem__(self, key):
        lin, col = key[0], key[1]
        return self.data[(lin, col)]
    
    def __setitem__(self, key, valor):
        lin, col = key[0], key[1]
        self.data[(lin,col)] = valor
        
    def crop(self, sup = 0, esq = 0, inf = True, dire = True):
        if inf == True:
            inf = len(self.data)
        if dire == True:
            dire = len(self.data[0])
                       
        crp = self.data[sup:inf, esq:dire]
        return NPImagem((1,1),crp)
        
    
    # escreva aqui os métodos da classe NPImagem
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()
