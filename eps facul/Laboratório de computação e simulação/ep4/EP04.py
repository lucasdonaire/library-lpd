#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#Escreva seus nomes e numeros USP
INFO = {12556552:"Lucas Panfilo Donaire",12556736:"Enzo Cappelozza"}

import numpy as np
import math
import pandas as pd


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
        n = 30000
        self.a = np.array(self.vetor_x)+np.array(self.vetor_y) #a = x+y
        self.b = np.array(self.vetor_x)*np.array(self.vetor_y) # b = x*y
        self.q = self.B(self.a) # quociente para usar em f()
        lt1 = []
        lt2 = []
        lt3 = []
        lz = []
        for i in range(n): # achar n pontos theta ~ dirichelet
            theta = []
            for i in range(3):
                theta += [np.random.gamma(self.a[i], 1)]
            vt = np.array(theta)/sum(theta)
            lt1.append(vt[0])
            lt2.append(vt[1])
            lt3.append(1-vt[0]-vt[1])
            val = self.f([vt[0],vt[1],1-vt[1]-vt[0]])
            lz.append(val)
                      
        self.lt1 = np.array(lt1) # lista de theta 1
        self.lt2 = np.array(lt2) # lista de theta 2
        self.lt3 = np.array(lt3) # lista de theta 3
        self.lz = np.array(lz) # lista de f(theta) para cada theta[i] = [lt1[i],lt2[i],lt3[i]]
        self.lzs = sorted(set(lz))
        self.max = max(self.lz) # ponto máximo de f
        v = np.linspace(0,self.max,200) # primeiro vetor V
        fv = self.fpinv(v)
        d = {'v':v, 'fv':fv}
        d = pd.DataFrame(d) # data frame para associar nossos v com fv=U(v)
        self.d = d
        vdif = self.vec_change(fv)
        qnt=0
        while(True): # esse while tem a intenção de gerar mais Vs onde temos que a diferença U(v[i]) - U(v[i-1]) é maior
        # ou seja, olhar melhor para onde a função é mais sensível às mudanças.
            if max(vdif) <  2: break ######
            vnf = []
            v = list(d['v']).copy()
            for i in range(1,len(vdif)):
                if vdif[i] >= 2: #####
                    vnovos = list(np.linspace(v[i-1],v[i],(vdif[i]//1) + 2))
                    vnovos = vnovos[1:len(vnovos)-1] # novos Vs
                    vnf.extend(vnovos)
            lv = list(d['v']).copy()
            lfv = list(d['fv']).copy()
            lv.extend(vnf)
            lfv.extend(self.fpinv(vnf))
            d = {'v':lv, 'fv':lfv};d = pd.DataFrame(d) # atualiza nosso d
            d = d.sort_values('v')
            self.d = d
            vdif = self.vec_change(list(d['fv'].copy()))
            if len(d['fv'].copy()) == qnt: break # se não aumentar a quantidade de pontos, paramos a função
            qnt = len(d['fv'].copy())
        self.d = d
        

    def U(self,v):
        """
        Este metodo recebe um valor para v e, a partir dele, retorna U(v|x,y) a partir dos 
        vetores x e y inicializados anteriormente
        """
        # Continue o codigo conforme achar necessario
        lv = np.array(list(self.d['v']).copy())
        lfv = np.array(list(self.d['fv']).copy())
        ld = list(abs(lv - v)) # qual v da nossa lista é mais proximo desse?
        idx = ld.index(min(ld))
        u =  lfv[idx]/len(self.lz) # proporção de pontos no cut-off set pelo total de pontos
        if abs(u-1)<0.0005:
            return 1
        else:
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
    # demorada, mas a chamada do metodo U(v) seja rapida. Ou seja, tente implementar
    # o maximo possivel do exercicio sem utilizar o valor de v. Desta forma, voce
    # pode acelerar o calculo de estimativas U(v) para diferentes valores de v 
    # sem precisar repetir todo o procedimento do exercicio para cada novo v.

    #-----------------------
   
   
    
    def fpinv(self,v):
        '''
        calcula quantos pontos estão abaixo de V (tamanho do 'cut-off set')
        '''
        pinv = []
        pinv.append(list(map(lambda x: self.pinvsup(x),v)))
        return pinv[0]
    
    def pinvsup(self,vi):
        lzs = self.lzs
        for z in lzs:
            if z >= vi: 
                idx = lzs.index(z)
                return(idx)
        return len(lzs)
        
 
    def f(self,theta):
        '''
        posterior density function
        '''
        tam = len(theta)
        p = 1
        for i in range(tam):
            p *= theta[i]**(self.a[i]-1)
        return p/self.q
    
    def B(self,a): # multivariate beta function
        '''
        '''
        soma = math.gamma(self.a.sum())
        prod = 1
        for i in range(3):
            prod *= math.gamma(self.a[i])
            

        return prod/soma
        
    
    def vec_change(self,v):
      ''''
      recebe vetor, retorna diferencas entre o índice do vetor e o anterior 
      (primeiro valor é sempre 0)
      usado para calcular quando parar de gerar novos Vs
      '''
    
      if len(v) < 2:return(0)
      vn = [0] * len(v)
      for i in range(1,len(v)):
        vn[i] = v[i] - v[(i-1)] 
      return vn






def main():
    #Coloque seus testes aqui
    print("Segue um exemplo de funcionamento:")
    print("Criando o objeto")
    estimativa = Estimador([5,6,2],[3,7,2])
    print()
    print(f"Os valores dos vetores utilizados sao: {estimativa.vetor_x,estimativa.vetor_y}")
    print("Este exemplo foi feito para demonstrar o funcionamento esperado do objeto")
    for i in range (1, 40):
        print(f"U({i}) = {estimativa.U(i)}")




if __name__ == "__main__":
    main()
    


