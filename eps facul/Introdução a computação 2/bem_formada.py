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

ABRE = '([{'
FECHA = ')]}'

def main():
    ''' função para teste da função bem_formada
    '''
    esp = '-=-' * 10
    
    print('deve ser True')
    st = '()()(){{}}{[()]}'
    print(bem_formada(st))
    print(esp)
    
    print('deve ser True')
    st = '(54)(oii)(2+5){sim{nao}nao}nao{[()]} [siiiiiiiim[]]'
    print(bem_formada(st))
    print(esp)
    
    print('deve ser False')
    st = '()()(){{}}{[()]}oiiiiii({)}}sim'
    print(bem_formada(st))
    print(esp)
    
    print('deve ser False')
    st = '()()(){{}}{[()]}oiiiiii({)}}sim{}}{{}()'
    print(bem_formada(st))
    print(esp)


# ---------------------------------------------------------
def inv(l):
    ''' (str) --> str 
    recebe um caracter que abre sequência: },] ou )
    retorna o correspondente que fecha: {,[ ou (                               
    '''

    if l == '}':
        return '{'
    elif l == ')':
        return '('
    elif l == ']':
        return '['


def bem_formada( seq ):
    ''' (str) -> bool
    Recebe uma string seq contendo uma sequência formada pelos
    caracteres '()[]{}'. 
    Retorna True caso a sequência esteja bem formada e False em
    caso contrário.
    A função deve ignorar caracteres diferentes de '()[]{}' 
    sem resultar em erro.
    Exemplos:
    >>> bem_formada( "(a+ {b })-{2*[3+4]}" )
    True
    >>> bem_formada( "( ( (  ) " )
    False
    >>> bem_formada( " { ( { x } )  } [ y ]" )
    True
    >>> bem_formada( " { ( { x }  } [ y ] )" )
    False
    '''
    tam = len(seq)
    l = []
    for carac in seq: #percorre a string
        if carac in ABRE:
            l += [carac] 
        if carac in FECHA:
            if l == []: # para nao dar erro de acesso ao index
                return False
            elif l[-1] == inv(carac):
                l.pop(-1)
            else:
                return False
            
    return l == []
        
    
# ---------------------------------------------------------

if __name__ == '__main__':
    main()