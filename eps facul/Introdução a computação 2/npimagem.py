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


# import numpy as np COELHO comentou isto que era do EG13 e não EI13
import numpy as np
## import matplotlib.pyplot as plt
## import matplotlib.image as mpimg

#from npimagem import NPImagem

def main2():
    fname = 'elvis.png'
    image = mpimg.imread(fname)
    gray = np.array(image)[:,:,2] ## pega canal G da imagem RGB

    elvis = NPImagem( (), gray ) # transforma o array em uma NPImagem
    print("elvis.shape: ", elvis.shape)
    plt.gray()
    plt.imshow(elvis.data)
    plt.show()

    fname = 'einstein.png'
    image = mpimg.imread(fname)
    gray = np.array(image)[:,:,2] ## pega canal G da imagem RGB

    einstein = NPImagem( (), gray)
    print("einstein.shape", einstein.shape)

    plt.imshow(einstein.data)
    plt.show()
    
    elvis.paste(einstein,20,450)
    plt.imshow(elvis.data)
    plt.show()

## ------------------------------------------------------------------
def main():

    lista = list(range(30))
    ar = np.array(lista).reshape(5,6)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")
    
    img2 = NPImagem( (3, 2), 100)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[1,2]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")
    
    img1.pinte_retangulo(1,2,3,5,99)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")
    
    img2.pinte_retangulo(-1,-2,1,2,88)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")
    
    img3.pinte_retangulo(1,0,3,4,77)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")
    
    
    img1.paste(img2, 1, 2)
    print(f"img1.paste(img2,1,2):\n{img1}\n")
    
    img1.paste(img3, 3, 5)
    print(f"img1.paste(img3,3,5):\n{img1}\n")
    
    img1.paste(img3, -1, -1)
    print(f"img1.paste(img3,-1,-1):\n{img1}\n")
    print("======Teste operadores\n")

    imgA = NPImagem( (2,3), 5)
    imgB = NPImagem( (), np.arange(20).reshape(5,4) )
    imgC = imgB.crop(2,1,4,4)
    imgD = imgA + imgC
    print(f"imgA:\n{imgA}")
    print(f"imgB:\n{imgB}")
    print(f"imgC:\n{imgC}")
    print(f"imgD:\n{imgD}")

    print("\n===== Crop ========\n")

    lista = list(range(30))
    ar = np.array(lista).reshape(6,5)
    img1 = NPImagem( (0, 0), ar)  # 
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem( (4, 3), 88)
    img3 = img2.crop() ## cria uma cópia
    img2[2,1] = -10
    print(f"img2[2,1]={img2[2,1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    print("======Teste pinte_retangulo\n")
    img1.pinte_retangulo(1,2,3,5,77)
    print(f"img1.pinte_retangulo(1,2,3,5,77):\n{img1}\n")

    img2.pinte_retangulo(-1,-2,2,3,99)
    print(f"img2.pinte_retangulo(-1,-2,2,3,99):\n{img2}\n")

    img3.pinte_retangulo(1,0,3,4,66)
    print(f"img3.pinte_retangulo(1,0,3,4,66):\n{img3}\n")

    print("======Teste paste\n")
    img1 = NPImagem( (0, 0), ar)  # 
    img2 = NPImagem( (2, 3), 99)
    img3 = img1.crop(2,1,5,3) ## cria uma cópia
    print(f"img1:\n{img1}")
    print(f"img2:\n{img2}")
    print(f"img3:\n{img3}")

    img1.paste(img2, 2, 3)
    print(f"img1.paste(img2,2,3):\n{img1}\n")

    img1.paste(img3, 4, 2 )
    print(f"img1.paste(img3,4,2):\n{img1}\n")

    img1.paste(img3, -1, 2)
    print(f"img1.paste(img3,-1,2):\n{img1}\n")
    
    imcop =img1.copy()
    print(img1)
    print(imcop)
    print(img1 + imcop)
    print(img1 * imcop)
    


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
        sup = max(sup, 0)
        esq = max(esq,0)
        inf = min(inf, self.shape[0])
        dire = min(dire, self.shape[1])
        
        crp = self.data[sup:inf, esq:dire]
        return NPImagem((1,1),crp.copy())
        
    def pinte_retangulo(self, sup, esq, inf, dire, v=0):
        self_nlins,  self_ncols = self.shape
        other_nlins, other_ncols = inf - sup, dire - esq
        

        if sup >= self_nlins or esq >= self_ncols\
           or inf <= 0  or dire <= 0: return

        #
        self_sup = max(0, sup)
        self_esq = max(0, esq)
        self_inf = min(sup + other_nlins, self_nlins)
        self_dir = min(esq + other_ncols, self_ncols)

        self.data[self_sup:self_inf, self_esq:self_dir] = v
        
        
    def copy(self):
        ndata = self.data[:]
        return NPImagem((0,0),ndata)
        
    def paste(self, other, sup, esq):
        '''(NPImagem, NPImagem, int, int) -> None
     Recebe um objeto NPImagem other e par de inteiros (sup, esq) 
     que indica um deslocamento em relação à origem de self (posição (0,0)) 
     onde a NPImagem other deve ser sobreposta sobre self. Observe que
     esse deslocamento pode ser negativo.
     '''
        self_nlins, self_ncols = self.shape
        other_nlins, other_ncols = other.shape

        # [inf, dir] é a posição mais a baixa e mais a direita de um possível 
        # pixel de self que será sobreposto 
        inf = sup + other_nlins
        dire = esq + other_ncols

        # se janela da sobreposição não tem pixel de self, retorne
        if sup >= self_nlins or esq >= self_ncols\
           or inf <= 0  or dire <= 0: return

        self_sup = max(0, sup)
        self_esq = max(0, esq)
        self_inf = min(inf, self_nlins)
        self_dir = min(dire, self_ncols)
        other_sup = -min(0, sup)
        other_esq = -min(0, esq)
        other_inf = other_sup + self_inf - self_sup
        other_dir = other_esq + self_dir - self_esq


        self.data[self_sup:self_inf, self_esq:self_dir] = other.data[other_sup:other_inf, other_esq:other_dir]
        
    
    def __add__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna a soma, elemento-a-elemento,
        dos pixels de self e other.
        '''
        if self.shape == other.shape:
            ndata = self.data + other.data
        else:
            ndata = self.data[:]
            for i in range(len(self.data)):
                for j in range(len(self.data[1])):
                    ndata[(i,j)] += other.data[(i,j)]
                    
        return NPImagem((0,0), ndata)
                    

    def __mul__(self, other):
        ''' (NPImagem, NPImagem) -> NPImagem
        Recebe dois objetos NPImagem e retorna o produto, elemento-a-elemento,
        dos pixels de self e other.
        '''
        if self.shape == other.shape:
            ndata = self.data * other.data
        else:
            ndata = self.data[:]
            for i in range(len(self.data)):
                for j in range(len(self.data[1])):
                    ndata[(i,j)] *= other.data[(i,j)]
                    
        return NPImagem((0,0), ndata)
                    
            
        # escreva aqui os métodos da classe NPImagem
## ------------------------------------------------------------------
## ------------------------------------------------------------------
if __name__ == '__main__':
    main()

