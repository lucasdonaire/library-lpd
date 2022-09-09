#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÃALHO 
# NÃO ALTERE OS NOMES DAS FUNÃÃES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Lucas Panfilo Donaire
    NUSP: 12556552

    Ao preencher esse cabeÃ§alho com o meu nome e o meu nÃºmero USP,
    declaro que todas as partes originais desse exercÃ­cio programa
    foram desenvolvidas e implementadas por mim ou por meu time 
    cujos nomes estÃ£o relacionados abaixo e que, portanto, nÃ£o 
    constituem desonestidade acadÃªmica ou plÃ¡gio.
    
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderÃ£o ser punidos por desonestidade acadÃªmica.

    Declaro tambÃ©m que sou responsÃ¡vel por todas as cÃ³pias desse
    programa e que nÃ£o distribui ou facilitei a sua distribuiÃ§Ã£o.
    
    Estou ciente que os casos de plÃ¡gio e desonestidade acadÃªmica
    estarÃ£o sujeitos Ã s penalidades descritas na pÃ¡gina da disciplina
    na seÃ§Ã£o "Sobre colaboraÃ§Ã£o em MAC0122".

    ReconheÃ§o que utilizei as seguintes fontes externas ao conteÃºdo 
    utilizado e recomendado em MAC0122, ou recebi auxÃ­lio das pessoas
    listadas abaixo, e incluo tambÃ©m os nomes de colegas
    do meu time caso essa tenha sido uma atividade em grupo.

    - LISTA de colegas do time 
        - nÃ£o foi uma atividade em grupo (substitua essa linha caso tenha sido)

    - LISTA de fontes externas utilizadas (links ou referÃªncias como livros)
        - 

    - LISTA de outras pessoas que colaboraram na realizaÃ§Ã£o do trabalho e
        externas ao grupo.
        - 
'''

# ===================================================================

class Complexo:
    '''Classe utilizada para representar um nÃºmero Complexo.

    Um complexo Ã© representado por dois nÃºmeros reais. 
    Assim, cada objeto dessa classe terÃ¡ dois atributos de estado:
 
       * `real`: um nÃºmero real que corresponde Ã  parte real
       * `imag`: um nÃºmero real que corresponde Ã  parte imaginÃ¡ria
 
    VocÃª deverÃ¡ escrever os mÃ©todos a seguir.
    '''

    #------------------------------------------------------------------------------
    def __init__(self, r = 0.0, i = 0.0):
        '''(Complexo, float, float) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referÃªncia `self` ao objeto que estÃ¡ sendo
        construÃ­do/montado e os reais `r` e `i` que 
        representam o nÃºmero complexo.

        Exemplos:

        >>> c0 = Complexo() # construtor chama __init__()
        >>> c0.real
        0.0
        >>> c0.imag
        0.0
        >>> c1 = Complexo(9)
        >>> print(c1.real, c1.imag)
        9.0 0.0
        >>> c2 = Complexo(9,4)
        >>> print(c2.real, c2.imag)
        9.0 4.0
        >>> 
        '''
        self.real = float(r)
        self.imag = float(i)
        
    #------------------------------------------------------------------------------        
    def __str__(self):
        '''(Complexo) -> str

        Recebe uma referencia `self` a um objeto da classe Complexo e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        FunÃ§Ã£o str() retorna a string criada pelo mÃ©todo __str__() da classe  

        Exemplos:

        >>> ini = Complexo(8)
        >>> fim = Complexo(9,4)
        >>> fim.__str__()
        '9.0+j4.0'
        >>> ini.__str__() # chamada do mÃ©todo __str__()
        '8.0'
        >>> str(ini) # funÃ§Ã£o str() exibe a string criada por __str__()
        '8.0'
        >>> str(fim) 
        '9.0+j4.0'
        >>> print(fim) # exibe o string criado por __str__()
        9.0+j4.0
        >>> print(ini)
        8.0
        >>>         
        '''
        if self.imag < 0:
            si = f'-j{abs(self.imag)}'
            
        elif self.imag == 0:
            si = ''
            
        elif self.imag > 0:
            si = f'+j{self.imag}'
            
        sr = f'{self.real}'
        
        return sr + si

    #------------------------------------------------------------------------------        
    def some(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referÃªncia `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado da soma self + other
        
        Exemplos:

        >>> c0 = Complexo(8)
        >>> c1 = Complexo(9,4)
        >>> c2 = c0.some(c1)
        >>> print(c2)
        17.0+j4.0
        >>>         
        '''
        r0 = self.real + other.real
        i0 = self.imag + other.imag
        return Complexo(r0, i0)
    

    #------------------------------------------------------------------------------        
    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo

        Recebe uma referencia `self` a um objeto da classe Complexo e
        outra referÃªncia `other`, para outro objeto Complexo, e cria e retorna
        um objeto Complexo resultado do produto self * other
        
        Exemplos:

        >>> comp0 = Complexo(1, 2)
        >>> comp1 = Complexo(3, 4)
        >>> comp2 = comp0 * comp1
        >>> print(c2)
        -5.0+j10.0
        >>>         
        '''
        
        r0 = self.real * other.real - (self.imag * other.imag)
        i0 = self.real * other.imag + self.imag * other.real
        return Complexo(r0, i0)
        
        


