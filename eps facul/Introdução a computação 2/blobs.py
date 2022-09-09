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


#------------
def main():
    x = [    
            8, 8, 8, 8, 1, 4,
            1, 8, 1, 1, 1, 4,
            1, 8, 8, 1, 4, 4,
            1, 1, 1, 1, 4, 4,
            1, 9, 1, 4, 1, 4,
            9, 9, 9, 9, 1, 4
        ]

    img = np.array(x).reshape(6,6)
    print(f'Imagem\n', img)

    # cria um objeto Blobs usando img
    blobs = Blobs(img)

    # vamos ver as blobs
    dt = blobs.data
    n = len(dt)
    for i in range(n):
        elem = list(dt[i])[0] # pega um elemento do conjunto
        print(f'blob {i} tem tamanho {len(dt[i])} e cor {img[elem]}')
        print(f'   {dt[i]}')
        
        
    b = blobs.segmente_blob(img, (0,0))
    print(b)
    blobs.pinte_blob(img, b, 99)
    print(img)
      


## ==================================================================

class Blobs:

    def __init__(self, img):
        ''' (Blobs, array) -> None 
        construtor da classe Blobs.
        '''

        self.data = []
        self.segmente(img) # deve carregar self.data
        ## inclua outros atributos que desejar

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Blobs) -> str
        retorna uma string com a descrição das blobs.
        '''
        
        txt = ''
        dt = self.data
        n = len(dt)
        for i in range(n):
            txt += f'blob {i} tem tamanho {len(dt[i])}\n'
            txt += f'   {dt[i]}\n'
        return txt

    # ---------------------------------------------------------------
    def segmente(self, img):
        ''' (Blobs, array) -> None
        Método usado pelo construtor para segmentar todas
        as blobs da imagem img.
        '''
        
        nlins, ncols = img.shape
        immark = [0] * (nlins * ncols)
        immark = np.array(immark).reshape(nlins, ncols)
        for i in range(nlins):
            for j in range(ncols):
                if immark[i, j] == 0:
                    blob = self.segmente_blob( img, (i,j) )
                    self.data += [blob]
                    for coord in blob:
                        immark[coord] = 1
                    
                    
                

    # ---------------------------------------------------------------
    def segmente_blob( self, img, semente ):
        ''' (Blobs, ndarray, tuple) -> set

            interface para o método self.segmente_blob_RM.
            Cria um conjunto vazio que é carregado
            de forma recursiva.  
            
            Não altere esse método.
        '''
        return self.segmente_blob_RM( img, semente, set() )

    # ---------------------------------------------------------------
    def segmente_blob_RM(self, img, semente, visitados ):
        ''' (Blobs, ndarray, tuple, set) -> set

        Recebe, além de self, um ndarray img e uma tupla semente contendo a
        coordenada de um pixel de img. Recebe também o conjunto
        visitados, que contém as coordenadas dos pixels já 
        visitados.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        
        if semente in visitados:
            return None
        
        
        visitados.add(semente)
        
          
        if semente[1] >= 1:
            sdir = (semente[0], semente[1] - 1)
            if img[semente] == img[sdir]:
                self.segmente_blob_RM(img, sdir, visitados)
                
        if semente[1] < img.shape[1] - 1:
            sesq = (semente[0], semente[1] + 1)
            if img[semente] == img[sesq]:
                self.segmente_blob_RM(img, sesq, visitados)
        
        if semente[0] >= 1:
            scima = (semente[0] - 1, semente[1])
            if img[semente] == img[scima]:
                self.segmente_blob_RM(img, scima, visitados)
                 
  
        if semente[0] < img.shape[0] - 1:
            sbaixo = (semente[0] + 1, semente[1])
            if img[semente] == img[sbaixo]:
                self.segmente_blob_RM(img, sbaixo, visitados)
        
                
        return visitados

    ## ==================================================================

    def pinte_blob( self, img, blob, nova_cor = 0):
        ''' (Blobs, ndarray, set, int) -> None

        Recebe, além de self, um ndarray img e um conjunto de pixels blob
        e pinta esses pixels com a nova_cor.

        Adapte esse método da função de mesmo nome implementada
        no exercício anterior.
        '''

        for pixel in blob:
            img[pixel] = nova_cor

## ==================================================================
## Coloque aqui outras funções e métodos que desejar
if __name__ == '__main__':
    main()

