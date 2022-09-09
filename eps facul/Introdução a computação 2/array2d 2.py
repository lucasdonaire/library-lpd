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

    # beginfora
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()

    b = a.reshape( (2,3) )   
    print(f'teste 2: reshape cria uma vista')
    print(b)
    print()
    
    print(f'teste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print(b)
    print()

    print(f'teste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1 
    print(a)
    print(b)
    print()

    print(f'teste 5: copy cria um clone')
    a = Array2d( (1,6), 3) # cria Array2d com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print(f'c: {c}')
    print()

    print(f'teste 6: mudanças em objeto um não devem refletir no outro')
    a[0,1] = 99
    c[0,5] = -1
    print(f'a: {a}')
    print(f'c: {c}')
    print()
    '''
    
    a = Array2d((3,2), 0)
    a[(0,1)] = 1
    a[(1,0)] = 2
    a[(1,1)] = 3
    a[(2,0)] = 4
    a[(2,1)] = 5
    print(a)
    
    print(f'lin 0 = {a.getlin(0)}')
    print(f'lin 1 = {a.getlin(1)}')
    print(f'lin 2 = {a.getlin(2)}')
    print(f'col 0 =\n {a.getcol(0)}')
    print(f'col 1 =\n {a.getcol(1)}')
     
    b = Array2d((1,6), 0)
    print(a.dot(b))
    c = Array2d((2,3), 2)
    print(a.dot(c))
    
    print("Testes da classe Array2d e comparação com Numpy\n")

    lista_a = [1, 2, 3, 4, 5, 6]
    lista_b = [0, 1, 1, 0, 0, 1]
    tam_a = len(lista_a)
    tam_b = len(lista_b)

    a = Array2d( (1, tam_a), 0) # cria Array2d com valor inicial 0
    print(f'teste 1: Criação do Array2d a:')
    print(a)
    print()
    a.data = lista_a   ## ou a.carregue(lista_a) como no EG10
    a.resize( (2,3) )
    print(f'a:\n{a}\n')

    b = Array2d( (1, tam_b), 0)
    b.data = lista_b   # ou b.carregue(lista_b)
    b.resize( (3,2) )
    print(f'b:\n{b}\n')

    linha = a.getlin(0)
    print(f'linha a[0,:] (=a.getlin(0))\n{linha}\n')

    coluna = b.getcol(1)
    print(f'coluna b[:,1] (=b.getcol(1))\n{coluna}\n')

    print(f'linha.dot(coluna)\n{linha.dot(coluna)}\n')

    print(f'matmul(a,b)\n{matmul(a,b)}\n')

    ### agora com Numpy
    import numpy as np
    npa = np.array( lista_a ).reshape((2,3))
    print(f'npa:\n{npa}\n')

    npb = np.array( lista_b ).reshape((3,2))
    print(f'npb:\n{npb}\n')

    print(f'np.matmul(npa, npb):\n{np.matmul(npa, npb)}\n')
    print('ao invés de np.matmul podemos usar @:')
    print(f'npa @ npb:\n{npa @ npb}\n')

## ==================================================================
#   A classe Array2d permite a manipulação de 'matrizes' de duas 
#   dimensões. O exercício é utilizar uma lista linear, ao invés
#   de uma lista aninhada, para armazenar os dados da matriz 
#   internamente.
#   A lista linear deve ser um atributo de nome 'data'.

class Array2d:

    # ---------------------------------------------------------------
    def __init__(self, shape, val):
        ''' (Array2d, tuple, obj) -> None
        Constrói um objeto do tipo Array2d com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        self.shape = shape
        self.size = shape[0] * shape[1]
        self.data = [val] * self.size

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2d, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2d self.

        Esse método é usado quando o objeto é chamado com 
        uma tupla entre colchetes, como self[0,0]. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        lin, col = key[0], key[1]
        return self.data[self.shape[1]*lin + col]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2d, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2d self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0. 
        Exemplo:
        >>> a = Array2d( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''
        lin, col = key[0], key[1]
        self.data[self.shape[1] * lin + col] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2d) -> None
        ao ser usada pela função print, deve exibir cada linha
        do Array2d em uma linha separada, separando seus elementos por um espaço.

        Exemplo: para self.data = [1, 2, 3, 4, 5, 6] e self.shape = (2,3)
        o método deve retornar a string 
        "1 2 3\n4 5 6" 
        e, caso self.shape = (3,2) o método deve retornar a string
        "1 2\n3 4\n5 6" 
        '''
        s = ''
        j = 0
        while j < self.size:
            s += str(self.data[j])
            s += ' '
            if (j+1) % self.shape[1] == 0:
                s += '\n'
            j += 1
            
        return s
    
    def resize(self, tup):
        if tup[0] * tup[1] == self.size:
            self.shape = tup
            
            
    def __mul__(self, other):
        nov = Array2d((self.shape), 0)
        if type(other) == float or type(other) == int:
            for i in range(self.size):
                nov.data[i] = self.data[i] * other
                
        if type(other) == Array2d:
            for i in range(self.size):
                nov.data[i] = self.data[i] * other.data[i]
                
        return nov
    
    def __rmul__(self, other):
        return self * other
    
    def __add__(self, other):
        nov = Array2d((self.shape), 0)
        if type(other) == float or type(other) == int:
            for i in range(self.size):
                nov.data[i] = self.data[i] + other
                
        if type(other) == Array2d:
            for i in range(self.size):
                nov.data[i] = self.data[i] + other.data[i]
                
        return nov
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        return self + (-1 * other)
    
    def __rsub__(self, other):
        return -1 * (self - other)
    
    def copy(self):
        cop = Array2d((self.shape),0)
        for i in range(self.size):
            cop.data[i] = self.data[i]
        return cop
    
    def reshape(self, tam):
        n = Array2d(tam, 0)
        n.data = self.data
        return n
    
    def getlin(self, lin):
        nlins, ncols = self.shape
        l = []
        for i in range(lin * ncols, lin* ncols + ncols):
            l += [self.data[i]]
            
        al = Array2d((1, ncols), 0)
        for i in range(ncols):
            al.data[i] = l[i]
        return al
    
    def getcol(self, col):
        nlins, ncols = self.shape
        l = []
        for i in range(col, col + nlins*ncols, ncols):
            l += [self.data[i]]
            
        ac = Array2d((nlins, 1), 0)
        for i in range(nlins):
            ac.data[i] = l[i]
            
        return ac
            
    
    def dot(self, other):
        n = 0
        for i in range(len(self.data)):
            n += self.data[i] * other.data[i]
            
        return n

#------------
    
def matmul(esq, dire):
    m, n1 = esq.shape
    n2, p = dire.shape
    na = Array2d((m,p), 0)
    l = []
    for i in range(m):
        for j in range(p):
            ee = esq.getlin(i)
            dd = dire.getcol(j)
            l += [ee.dot(dd)]
    na.data = l
    return na

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar
'''
def getlin(self, lin): 
    que recebe um Array2d self e um inteiro lin e um Array2d 
    formado pela a linha de índice lin de self.

def getcol(self, col): que recebe um Array2d
 self e um inteiro col e um Array2d formado 
 pela coluna de índice col de self.

def dot(self, other): que recebe um Array2d 
self e outro Array2d other com o mesmo número
 de elementos (size), e retorna um número (escalar) 
resultante da soma do produto termo a termo entre self e other.

Além desses 3 métodos, implemente também a função:

def matmul( esq, dir ): que recebe um Array2d es
q de dimensão (m, n) e outro Array2d dir de dimensão (n, p) e retorna o produto matricial entre 
esq e dir, que deve ser outro Array2d de dimensão (m, p).
'''




## ==================================================================

if __name__ == '__main__':
    main()