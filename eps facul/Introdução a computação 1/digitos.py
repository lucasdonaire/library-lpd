# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
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

'''

# escreva seu programa a seguir

n = int(input('Digite n: '))

exp = 1

while n >= 10**exp:
    exp = exp + 1
    
exp3 = exp
exp2 = exp

m = 1
s1 = 0
while exp3 > 0:
    s1 = s1 + m * ((n % (10**exp3) - n % (10**(exp3 -1)))/(10**(exp3 -1)))
    exp3 = exp3 - 1
    m = m + 1

r1 = s1 % 11
if r1 == 0 or r1 == 10:
    dv1 = 0
else:
    dv1 = r1

m1 = 0
s2 = 0
while exp2 > 0:
    s2 = s2 + m1 * ((n % (10**exp2) - n % (10**(exp2 -1)))/(10**(exp2 -1)))
    exp2 = exp2 - 1
    m1 = m1 + 1

s2n = s2 + exp*dv1

r2 = s2n % 11
if r2 == 0 or r2 == 10:
    dv2 = 0
else:
    dv2 = r2

dv1 = int(dv1)    
dv2 = int(dv2)

print(f'DVs = {dv1} {dv2}')







