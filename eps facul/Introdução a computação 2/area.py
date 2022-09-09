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
import random

## ==================================================================
# 
def main():
    '''
    Testes da classe AreaCirculo

    inclua mais 10 testes distintos.
    '''

    print("Testes do EI28 - Método Científico")
    
    r,n,t = 100, 100, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1, 100, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1, 1000, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1, 10, 10000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1, 10000, 10
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1, 1, 1
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 50, 100, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 200, 100, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 1000, 1000, 1000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    r,n,t = 100, 5000, 5000
    a = AreaCirculo(r, n, t)
    print(a)
    print(f'area mesmo = {np.pi * r**2}')
    print()
    
    
    
    


## ==================================================================
# 
class AreaCirculo:

    #------------------------------------------
    def __init__(self, r=100, n=100, t=1000):
        '''(AreaCirculo, float, int, int) -> None

        RECEBE um número r (float ou int), um inteiro n e um inteiro t.
        CALCULA uma estimativa self.area_circulo para a área do circulo de raio r. 

        Para determinar a estimativa são realizados t experimentos em que 
        cada experimento calcula uma estimativa para a área do um quadrante 
        do círculo de raio r. 

        A estimava para a área do círculo é a média aritmética das estimativas. 
        '''
        self.r = r    # raio do círculo
        self.foto = tire_foto(r)  # simula o sensor
        self.area_sombra = 4*self.sombra() # area pelo numero de pixels da sombra

        self.n = n    # número de pontos
        self.t = t    # número de experimentos
        # calcule a soma das t estimativas das áreas dos quadrantes
        soma_area_quadrantes = 0  # area por amostragem
        for i in range(t):
            soma_area_quadrantes += self.experimento()
        # calcule a estimativa para a área do quadrante    
        area_quadrante = soma_area_quadrantes/t
        # calcule a estimativa para a área do círculo
        self.area_circulo = 4*area_quadrante

    #------------------------------------------    
    def __str__(self):
        '''(AreaCirculo) -> str
        RETORNA uma string que representa self e pode ser usada por print() e str().
        '''
        return f"AreaCirculo({self.r}, {self.n}, {self.t}) = {self.area_circulo} | sombra = {self.area_sombra}"
    
    #------------------------------------------    
    def area(self):
        '''(AreaCirculo) -> float
        RETORNA uma estimativa para a área do círculo de raio self.r
        '''
        return self.area_circulo

    #------------------------------------------    
    def sombra(self):
        '''(AreaCirculo) -> float
        RETORNA a área da sombra em pixels da foto
        '''
        f = self.foto
        ns = np.count_nonzero( f == 0 ) 
        return ns
    
    #-----------------------------------------
    def experimento(self):
        '''(AreaCirculo) -> float
        REALIZA um experimento em que são sorteados self.n pontos 
            no quadrado de veŕtices (0,0) e (self.r, self.r). 
            A resposta do sensor para cada ponto (x,y) sorteado
            está na imagem binária (ndarray) self.foto.
        RETORNA uma estimativa para a área do quadrante do círculo de 
           raio self.r.
        A estimativa é o produto da área do quadrado pela fração de 
           pontos sorteados no quadrante.

        Para escrever este método considere usar random.randrange(r)
        https://docs.python.org/3/library/random.html
        '''
        # implemente sua solução
        cont = 0
        for i in range(self.n):
            x, y = self.r * random.random(), self.r * random.random()
            if x**2 + y**2 <= self.r**2:
                cont += 1
        
        proporcao = cont/self.n
        #print(proporcao)
        area = proporcao * self.r**2
        return(area)

## ==================================================================
SENSOR = 1
SOMBRA = 0

def tire_foto( r ):
    ''' (int) -> ndarray

    cria uma imagem binária do nosso objeto de estudo, 
    um quadrante de um círculo de raio r em um fundo quadrado 
    de lado r.
    Retorna uma imagem, um numpy.ndarray, resolução r x r.
    '''
    foto = np.full( (r,r), SENSOR) # sensor 
    for x in range(r):
        for y in range(r):
            if x*x + y*y < r*r:
                foto[x,y] = SOMBRA  # sombra
    return foto

## ==================================================================
# 
if __name__ == '__main__':
    main()
