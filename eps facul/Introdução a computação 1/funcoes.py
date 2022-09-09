# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: Lucas Panfilo Donaire
    NUSP: 12556552

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

"""

#----------------------------------------------------    
def primo(n):
    '''(int) -> bool

       RECEBE um número inteiro n.
       RETORNA True se n é primo e False em caso contrário.
    '''
    # remova o print() e escreva suas função a seguir 
    i = 3
    prim = True
    if (n % 2 == 0 and n != 2) or n <= 1:
        prim = False
    while i < n/2 and prim == True:
        if n % i == 0:
            prim = False
        i = i + 2
    return prim

#----------------------------------------------------        
def goldbach(n):
    '''(int) -> bool, int, int 

       RECEBE um número inteiro n.
       RETORNA True, p, q se n é soma de dois números primos p e q.
       Se n não é soma de dois números primos a função retorna False, 1, 1.
    '''
    # remova o print() e escreva suas função a seguir 
    soma = False
    p = 2
    while p <= n:
        q = 2
        while q <= n:    
            if primo(p) and primo(q) == True and p + q == n:
                soma = True
                return soma, p, q
               
            q = q + 1 + (q % 2)
        p = p + 1 + (p % 2)
    if soma == False:
        return False, 1, 1

#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * um inteiro d,  d >=  0. 

      RETORNA o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    result = (n0 * (1 + e*p )**d)
    return int(result)
      
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(int, int, float, int, int) -> int
 
       RECEBE 

         * o número n0 de indivíduos infectados em um dia 0;
         * o número diário médio e de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade p de uma exposição resultar em uma infecção;
         * o número n de indivíduos na população; e
         * um inteiro d, d >= 0. 

       RETORNA o número total de indivíduos infectados até o dia d 
       determinado por (n0, e, p, n).

    '''
    dn = n0
    i = 0
    while i < d:
        frac = dn/n
        ctt = e * p
        dn = dn*(1 + (ctt *(1 - frac)))
        i = i + 1
    return int(dn)
