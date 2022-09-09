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
def main():

    t1 = Horario(8,0,0)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1,40)
    print(f't2 = {t2} e deve ser 01:40:00')

    t3 = t1 + t2
    print(f't3 = {t3} e deve ser 09:40:00')

    t4 = t1 + Horario(0,100)  ## 100 minutos equivale a 01:40
    print(f't4 = {t4} e deve ser 09:40:00') 

    print(f't4 == t3 é {t4 == t3} e deve ser True')
    print(f't1 >  t2 é {t1 >  t2} e deve ser True')
    print(f't1 >= t2 é {t1 >= t2} e deve ser True')
    print(f't1 <  t2 é {t1 <  t2} e deve ser False')
    print(f't1 <= t2 é {t1 <  t2} e deve ser False')
    print(f't1 == t2 é {t1 == t2} e deve ser False')

    t5 = Horario(23,59,59)
    t6 = Horario(0,0,1)
    t7 = t5 + t6
    print(f't7 = {t7} e deve ser 00:00:00')

    t8 = t1 - t2  
    print(f't8 = {t8} e deve ser 06:20:00')

    t9 = t2 - t1   ##   nao temos horarios negativos
    print(f't9 = {t9} e deve ser 00:00:00')

    print(f't2.dados = {t2.dados} e deve ser a lista [0, 40, 1]')
    
    

    

class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.
 
       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve se "comportar" ilustrados no enunciado.
    '''
    
    def __init__(self, horas = 0, minutos = 0, segundos= 0):
        
        if 0 <= segundos <= 59:
            s = segundos
        elif segundos > 59:
            minutos += segundos // 60
            s = segundos % 60
        
        if 0 <= minutos <= 59:
            m = minutos
        elif minutos > 59:
            horas += minutos // 60
            m = minutos % 60
            
        if 0 <= horas <= 23:
            h = horas
        elif horas > 23:
            h = horas % 24
            
        self.dados = [s, m, h]
  
        
  
    def zeros(self, n):
        '''
        Recebe n, inteiro entre 0 e 100
        retorna uma string que faz n ocupar 2 espaços
        Exemplos
        zeros(1) = 01
        zeros(0) = 00
        zeros(30) = 30    
        '''
        if n < 10:
            st = '0' + str(n)
        elif n < 100:
            st = str(n)
            
        return st
        
    
    
    def __str__(self):
        l = [ self.zeros(self.dados[2]), self.zeros(self.dados[1]), self.zeros(self.dados[0])]
        return f'{l[0]}:{l[1]}:{l[2]}'
    
        
    
    def __add__(self, other):
        ns = self.dados[0] + other.dados[0]
        nm = self.dados[1] + other.dados[1]
        nh = self.dados[2] + other.dados[2]
        
        return Horario(nh, nm, ns)
    
    def __sub__(self, other):
        
        if self < other:
            return Horario(0,0,0)
        
        ns = self.dados[0] - other.dados[0]
        nm = self.dados[1] - other.dados[1]
        nh = self.dados[2] - other.dados[2]
        
        if min(ns, nm, nh) >= 0:    
            return Horario(nh, nm, ns)
        else:
            if ns < 0:
                nm -= (abs(ns) // 60) + 1
                ns = 60 - (abs(ns) % 60)
            if nm < 0:
                nh -= (abs(nm) // 60) + 1
                nm = 60 - (abs(nm) % 60)
            if nh < 0:
                nh = 24 - (abs(nh) % 24)
            
            return Horario(nh, nm, ns)
        
    
    
    def __eq__(self, other):
        return self.dados == other.dados
         
    
    def __gt__(self, other):
        if self == other:
            return False
        
        elif self.dados[2] > other.dados[2]:
            return True
        elif self.dados[2] < other.dados[2]:
            return False
        else:
            if self.dados[1] > other.dados[1]:
                return True
            elif self.dados[1] < other.dados[1]:
                return False
            else:
                if self.dados[0] > other.dados[0]:
                    return True
                elif self.dados[0] <= other.dados[0]:
                    return False
                
    def __ge__(self, other):
        if self == other:
            return True
        else:
            return self > other
        
        
    def __lt__(self, other):
        if self == other:
            return False
        else:
            return not self > other
        
    def __le__(self, other):
        if self == other:
            return True
        else:
            return not self > other
        


# ------------------------------------------------------------
if __name__ == "__main__":
    main()