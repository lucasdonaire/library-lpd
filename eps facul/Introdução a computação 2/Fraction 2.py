# -*- coding: utf-8 -*-
# 
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------

'''

    Nome: Lucas Panfilo Donaire
    NUSP: 12556552

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa
    foram desenvolvidas e implementadas por mim e que, portanto, não 
    constituem desonestidade acadêmica ou plágio.
    
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
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

# ===================================================================

def main():
    '''
        Programa main usado para teste da classe Fraction.
    '''

    # Criação de objetos do tipo Fraction 
    f12 = Fraction(1,2)
    f34 = Fraction(3,4)

    # soma 2 fracoes
    soma = f12 + f34
    print(f"{f12} + {f34}      = {soma}")
    print(f"Resultado esperado = 5/4 ")

    # soma fracao com inteiro
    soma = f12 + 2
    print(f"{f12} + 2         = {soma}")
    print(f"Resultado esperado = 5/2 ")

    # soma inteiro com fracao
    soma = 2 + f34
    print(f"  2 + {f34}      = {soma}")
    print(f"Resultado esperado = 11/4 ")

    # ===================================================================
    # Escreva outros testes
    soma = f12 / 2
    print(f"{f12} / 2         = {soma}")
    print(f"Resultado esperado = 1/4 ")
    
    soma = f12 / f34
    print(f"{f12} / {f34}         = {soma}")
    print(f"Resultado esperado = 2/3 ")
    
    soma = 4/ f12
    print(f"4 / {f12}         = {soma}")
    print(f"Resultado esperado = 8/1 ")
    
    soma = 4 == Fraction(4,1) 
    print(f"4 == Fraction(4,1)       = {soma}")
    print(f"Resultado esperado = True ")
    
    soma = 4 == Fraction(8,2) 
    print(f"4 == Fraction(8,2)       = {soma}")
    print(f"Resultado esperado = True ")
    
    soma = 4 == Fraction(7,3) 
    print(f"4 == Fraction(7,3)       = {soma}")
    print(f"Resultado esperado = False ")
    
    soma = Fraction(4, 1) == Fraction(4,1) 
    print(f" Fraction(4,1) == Fraction(4,1)       = {soma}")
    print(f"Resultado esperado = True ")
    
    soma = Fraction(8, 2) == Fraction(4,1) 
    print(f" Fraction(8,2) == Fraction(4,1)       = {soma}")
    print(f"Resultado esperado = True ")
    
    soma = Fraction(4, 1) == Fraction(7,3) 
    print(f" Fraction(4,1) == Fraction(7,3)       = {soma}")
    print(f"Resultado esperado = False ")
    
    soma = Fraction(4, 1) == 4
    print(f" Fraction(4,1) == 4       = {soma}")
    print(f"Resultado esperado = True ")
    
    soma = Fraction(4, 1) == 3
    print(f" Fraction(4,1) == 3       = {soma}")
    print(f"Resultado esperado = False ")
    
    


# ===================================================================
#
#   No futuro substituiremos a definição da classe por um import. 
#
# ===================================================================

def reduz(x, y):
    menor = min(abs(x), abs(y))
    i = menor   
    while i > 0:
        if x % i == 0 and y % i == 0:
            x = x/i
            y = y/i
        i -= 1
        
    return int(x), int(y)
    

class Fraction:
    '''
        Essa classe Fraction foi adaptada da seção 1.13.1 Uma Classe Fraction
        do capítulo 1 do livro Resolução de Problemas com Algoritmos e 
        Estruturas de Dados usando Python disponível no endereço
        https://panda.ime.usp.br/panda/static/pythonds_pt/index.html. 

        A classe Fraction representa uma fração. 
        Uma fração é constituída por um numerador e um denominador, 
        ambos inteiros, como por exemplo 2/5 (dois quintos), 
        onde 2 é o numerador e 5 o denominador.
    '''

    def __init__(self, cima, baixo):
        '''(Fraction, int, int) --> None

        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído/montado e os inteiros cima e baixo que representam
        a fração.

        Exemplos:

        >>> frac = Fraction(2,5) # construtor chama __init__()
        >>> frac.num
        2
        >>> frac.den
        5
        '''
        self.num = cima
        self.den = baixo

    def __str__(self):
        '''(Fraction) -> str

        Recebe uma referencia `self` a um objeto da classe Fraction e
        cria e retorna a string que representa o objeto.

        Utilizado por print() para exibir o objeto.
        Função str() retorna a string criada pelo método __str__() da classe  

        Exemplo:

        >>> frac = Fraction(2,5)
        >>> print(frac)
        2/5
        '''
        return f"{self.num}/{self.den}"

    #------------------------------------
    def __add__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a soma da Fraction `self` e da Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction + Fraction ou
                                            Fraction + int
        """
        
        if type(other) == Fraction:
            snum = self.num * other.den + self.den * other.num
            sden = self.den * other.den
            
            snum, sden = reduz(snum,sden)
            
            return Fraction(snum, sden)
        
        if type(other) == int:
            snum = self.num + self.den * other
            sden = self.den
            
            snum, sden = reduz(snum,sden)
            
            return Fraction(snum, self.den)
            
    #------------------------------------
    def __radd__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a soma da Fraction `self` e int `other`.
        Usado pelo Python quando escrevemos int + Fraction
        """
        snum = self.num + self.den * other
        sden = self.den
            
        snum, sden = reduz(snum,sden)
            
        return Fraction(snum, self.den)
        

    #-------------------------------------
    def __truediv__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a divisão da Fraction `self` pela Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction / Fraction ou
                                            Fraction / int
        """
        if type(other) == Fraction:    
            dnum = self.num * other.den
            dden = self.den * other.num
            dnum, dden = reduz(dnum, dden)
            
            return Fraction(dnum, dden)
        
        if type(other) == int:
            dnum = self.num 
            dden = self.den * other
            dnum, dden = reduz(dnum, dden)
            
            return Fraction(dnum, dden)
            
        

    #-------------------------------------
    def __rtruediv__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a divisão do int `other` pela Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        dnum = self.den * other
        dden = self.num
        dnum, dden = reduz(dnum, dden)
        
        return Fraction(dnum, dden)
        


    #-------------------------------------
    def __eq__(self, other):
        """ (Fraction, Fraction ou int) -> Fraction

        Retorna a comparação da Fraction `self` com a Fraction ou int `other`.
        Usado pelo Python quando escrevemos Fraction == Fraction ou
                                            Fraction == int
        """
        if type(other) == int:
            c = self.num / self.den
            return c == other
            
        if type(other) == Fraction:
            c = self.num * other.den
            c2 = self.den * other.num
            return c == c2

    #-------------------------------------
    def __req__(self, other):
        """ (Fraction, int) -> Fraction

        Retorna a comparação do int `other` com a Fraction `self`.
        Usado pelo Python quando escrevemos int / Fraction
        """
        
        c = self.num / self.den
        return c == other
        

## =============================================================
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================
if __name__ == "__main__":
    main()