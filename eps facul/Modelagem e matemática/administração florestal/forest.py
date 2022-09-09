"""
Trabalho desenvolvido para o curso MAP2210 - Modelagem e Matemática

Desenvolvido pelos alunos:
Enzo Valentim Cappeloza Nº USP 12556736
Henrique Fujikawa Tokunaga NºUSP 12675207
Lucas Panfilo Donaire Nº USP 12556552
Marcos Martins Marchetti Nº USP 11910868
Ygor Peniche Maldonado Nº USP 10271558
"""

import numpy as np


def get_matrices():
    """
    Obtém do usuário os valores para:
    Classes: Agrupamento das ávores conforme as suas faixas de alturas.
    Preços: Preços das árvores que estão em cada classe.
    Crescimeto: Taxa de crescismento de quantas ávores passam de uma classe para outra em cada período.
    :return: o valor das classes, preços e taxa de crescimento.
    """
    # variável que armazena a quantidade de classes das alturas das ávores
    classes = None

    # dicionário que armazena os preços de cada classe
    precos = {}

    # dicionário que armazena as taxas de ccrescimento de cada classe
    crescimento = {}

    # variáveis que controlam as entradas do usuário
    classes_flag = True
    precos_flag = False
    crescimento_flag = False
    while True:

        # recebe do usuário as entradas da quantidade de classe
        if classes_flag:
            classes = int(input('\nDigite quantas classes de ávores existem: '))
            correto = input(f'\nConfirma a quantidade de {classes} classes? [S/N] ').lower()

            if correto == 's':
                classes_flag = False
                precos_flag = True

        # recebe do usuário as entradas referente aos preços de cada classe
        if precos_flag:

            # o preço da primeira classe ecebe o valor de $0,00, conforme explicado no trabalho
            precos['classe_1'] = 0.00

            for i in range(2, classes + 1):
                precos[f'classe_{i}'] = float(input(f'\nInforme o preço das árvores na classe {i} (Ex.: 150.00): '))

            correto = input(f'\nOs preços estão corretos? \n{precos} \n[S/N] ').lower()
            if correto == 's':
                precos_flag = False
                crescimento_flag = True

        # recebe do usuário as taxas de crescimento de cada classe
        if crescimento_flag:
            for i in range(1, classes):
                crescimento[f'classe_{i}'] = float(input(
                    f'\nInforme a taxa de crescimento das árvores na classe {i} para a classe {i+1} (Ex.: 0.2): '))

            correto = input(f'\nAs taxas de crescimento estão corretas? \n{crescimento} \n[S/N] ').lower()
            if correto == 's':
                break

    return classes, precos, crescimento


def calculate_matrices(classes, preco, crescimento):
    """
    Realiza o cálculo do retorno ótimo sustentável.
    :param classes: Quantidade de classes.
    :param preco: Matriz com os preços das árvores.
    :param crescimento: Matriz contendo as taxas de crescimento.
    :return: Exibe na tela a matriz resultado, o valor e classe do retorno ótimo sustentável.
    """
    # converte em numpy array para podermos realizar operações com matrizes
    matrix_price = np.array(list(preco.values()))
    matrix_growth = np.array(list(crescimento.values()))

    # lista que armazena os resultados
    matrix_result = [.0]
    for i in range(1, classes):

        # itera em cada classe e realiza os cálculos das matrizes.
        # cálculo demonstrado na questão 3
        result = (matrix_price[i] / np.sum(1 / matrix_growth[:i]))
        matrix_result.append(result)

    # salva em numpy array os resultado do cálculo anterior
    matrix_result = np.array(matrix_result)

    # armazena o maior valor obtido no cálculo
    optimal_return = np.max(matrix_result)

    # armazena o número da classe que obteve o maior valor
    optimal_class = np.argmax(matrix_result) + 1

    print(f'\nA matriz dos preços é representada por:\n{matrix_price}')
    matrix_growth = np.append(matrix_growth, np.NAN)
    print(f'\nA matriz das taxas de crescimento é representada por:\n{matrix_growth}')
    print(f'\nA Matriz de retorno ótimo é representado por:\n{matrix_result}')
    print(f'\nA Classe com retorno ótimo é a {optimal_class}ª, com o valor de {round(optimal_return, 4)}')


if __name__ == '__main__':
    # inicia o código
    print('Sistema de Retorno Máximo para um Plantio Sustentável.')
    cl, pr, cr = get_matrices()
    calculate_matrices(cl, pr, cr)
