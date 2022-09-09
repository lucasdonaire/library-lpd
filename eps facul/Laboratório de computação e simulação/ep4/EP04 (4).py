#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math


#Escreva seus nomes e numeros USP
INFO = {12556906:"Daniel Epelbaum",4206942666:"Darth Vader"}


class Estimador:
    """
    Classe para criar o objeto, ele recebe valores para os vetores x e y.
    Os metodos definidos abaixo serao utilizadas por um corretor automatico. Portanto,
    precisa manter os outputs e inputs dos 2 metodos abaixo. 
    """
    def __init__(self,x,y):
        """
        Inicializador do objeto. Este metodo recebe 
        valores pros vetores x e y em formato de lista 
        e implementa no objeto. 
        """
        self.vetor_x = x #formato: [0,0,0] - List cujo len(x) = 3
        self.vetor_y = y #formato: [0,0,0] - List cujo len(y) = 3
        #Continue o codigo conforme achar necessario.
        
        a = [x[i]+y[i] for i in range (3)]
        k = 2000
        n = 40000
        B = math.factorial(sum(a)-1)/(math.factorial(a[0]-1)*math.factorial(a[1]-1)*math.factorial(a[2]-1))
        F = []
        for i in range (n):
            t1, t2, t3 = np.random.dirichlet(a)
            f = B*(t1**(a[0]-1))*(t2**(a[1]-1))*(t3**(a[2]-1))
            F.append(f)
        sup = (n+1)/n * max(F)
        V = [sup*i/k for i in range (k+1)]
        U = [0 for i in range (k+1)]        
        for i in range (1, k+1):
            p = U[i-1]
            j = len(F) - 1
            while j >= 0:
                if F[j] < V[i]:
                    p += 1
                    F.remove(F[j])
                j -= 1
            U[i] = p
        self.V = V
        self.Uv = [U[i]/n for i in range (k+1)]


    def U(self,v):
        """
        Este metodo recebe um valor para v e, a partir dele, retorna U(v|x,y) a partir dos 
        vetores x e y inicializados anteriormente
        """
        # Continue o codigo conforme achar necessario
        
        p = 0
        k = len(self.V) - 1
        while v > self.V[p] and p < k:
            p += 1

        if p == k:
            u = 1
        if v == self.V[p] and p < k:
            u = self.Uv[p]
        if v < self.V[p] and p < k:
            u = self.Uv[p-1] + (self.Uv[p] - self.Uv[p-1])*k/max(self.V)*(v - self.V[p-1])

        #u = f"--'Coloque aqui a sua estimativa para U({v}|x,y)'--" 
        return u


    ############################################################################
    # Escreva aqui embaixo qualquer outro metodo ou funcao que voce queira utilizar no
    # exercício. Pedimos que mantenha o nome dos metodos ja definidos acima, 
    # os inputs do __init__() e do U() precisam ser mantidos iguais, assim como
    # os outputs.
    # ela implemente a estimativa U(v). Esse formato utilizado e demonstrado no
    # main sera utilizado pelo corretor automativo.
    # 
    # Exemplo de funcionamento do corretor:
    # 
    #           from EP04 import estimador
    #           estimativa_do_aluno = estimador([1,2,3],[4,5,6])
    #           if abs(estimativa_do_aluno.U(7) - W(7)) <= 0.0005:
    #               print("Parabens, mais 5 na nota") 
    #           if abs(estimativa_do_aluno.U(0.2) - W(0.2)) <= 0.0005:
    #               print("Parabens, mais 5 na nota")
    # 
    ############################################################################

    # Dica: Tente implementar o Estimador() de tal forma que a inicializacao seja
    # demorada, mas a chgamada do metodo U(v) seja rapida. Ou seja, tente implementar
    # o maximo possivel do exercicio sem utilizar o valor de v. Desta forma, voce
    # pode acelerar o calculo de estimativas U(v) para diferentes valores de v 
    # sem precisar repetir todo o procedimento do exercicio para cada novo v.




def main():
    #Coloque seus testes aqui
    print("Segue um exemplo de funcionamento:")
    print("Criando o objeto")
    estimativa = Estimador([1,2,3],[4,6,4])
    print("Implementando o valor para v")
    print(f"Temos que U({42}) = {estimativa.U(42)}")
    print(f"Para um novo valor de v, temos que U({5/4}) = {estimativa.U(5/4)}")
    print()
    print(f"Os valores dos vetores utilizados sao: {estimativa.vetor_x,estimativa.vetor_y}")
    print("Este exemmplo foi feito para demonstrar o funcionamento esperado do objeto")
    for i in range (1, 20):
        print(f"U({i}) = {estimativa.U(i)}")


if __name__ == "__main__":
    main()