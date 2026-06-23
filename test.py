from treinamento import treinar
from ativacoes import sigmoid, sigmoid_derivada
from rede import rede

entradas = [18, -9, 56, 444, 54, 1, 33, 99, 0]

pesos_list = [[[0, 0, 7, 9, 2, 99, 81, 2, 12], [0, 1, 7, 9, 22, 19, 81, 2, 1], [10, 20, 7, 9, 32, 9, 8, 2, 2]], [[3, 0, 0, 0, 5, 18, 6, 2, 1], [1, 17, 19, 7, 5, 1, 23, 9, 0]]]

bias_list = [ [0.5, 1, 0.2], [1, 0.1] ]

pesos = [0.1]*9
bias = 0.5

esperado = 1

lr = 0.1

for epoca in range(10000):
    saida, pesos, bias = treinar(
        entradas, pesos, bias,
        esperado, lr,
        ativacoes=sigmoid,
        derivada=sigmoid_derivada
    )
    if epoca % 1000 == 0:
        print(epoca, saida)

saidas = rede(entradas, pesos_list, bias_list, sigmoid)

def decisao_final(saidas):
    return saidas.index(max(saidas))

indice = decisao_final(saidas)

clases = ["não", "sim"]

resposta = clases[indice]

print(f"    A respectiva resposta é: {saida}")