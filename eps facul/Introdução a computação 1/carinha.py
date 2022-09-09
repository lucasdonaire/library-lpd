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

##################################################################
## ESCREVA SEU PROGRAMA ABAIXO

x = float(input('Digite x: '))
y = float(input('Digite y: '))
cor = 'azul'

if x>8 or x<0 or y>8 or y<0:
    cor = 'branco'

elif (1>x>=0 or 7<x<=8) and 2>y>=0:
    cor = 'branco'
    
elif 3<x<5 and 1.5<y<2.5:
    cor = 'branco'

elif ((x-3)**2 + (y-2)**2) < 0.25:
    cor = 'branco'
    
elif ((x-5)**2 + (y-2)**2) < 0.25:
    cor = 'branco'
    
elif 3.5<=x<=4.5 and 3.5<=y<=4.5:
    cor = 'branco'

elif (1<=x<=3 or 5<=x<=7) and 7.25<=y<=7.75:
     cor = 'branco'

elif 1 >= (x-2)**2 + (y-6)**2> 0.25:
     cor = 'branco'

elif 1 >= (x-6)**2 + (y-6)**2> 0.25:
     cor = 'branco'
     
print(cor)