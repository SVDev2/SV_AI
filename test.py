#x1 = 19
#w1 = 4

#resultado = x1 * w1

#print("    ", resultado)

#########

#x2 = 4
#w2 = 8

#resultado = x1*w1 + x2*w2

#print(f"    A resposta é: {resultado}")

#########

#bias = -5

#resultado = x1*w1 + x2*w2 + bias

#print(f"    O respectivo resultado é {resultado}")

#########

#if resultado > 10:
#    saida = 1
#else:
#    saida = 0
#    
#print(f"    Resultado: {resultado}")
#print(f"    Saida: {saida}")

#########

#entradas = [18, -9, 56, 444, 54, 1, 33, 99, 0]

#pesos = [0, 0, 7, 9, 22, 99, 81, 2, 12]

#resultado = entradas[0]*pesos[0] + entradas[1]*pesos[1] + entradas[2]*pesos[2] + entradas[3]*pesos[3] + entradas[4]*pesos[4] + entradas[5]*pesos[5] + entradas[6]*pesos[6] + entradas[7]*pesos[7] + entradas[8]*pesos[8]

#print(f"    o resultado é: {resultado}")

#########

#entradas = [18, -9, 56, 444, 54, 1, 33, 99, 0]

#pesos = [0, 0, 7, 9, 22, 99, 81, 2, 12]

#total = 0

#for entrada, peso in zip(entradas, pesos):
#    total += entrada*peso

#print(f"    o resultado é: {total}")

#########

from ativacoes import sigmoid
from rede import rede

entradas = [18, -9, 56, 444, 54, 1, 33, 99, 0]

pesos_list = [[[0, 0, 7, 9, 2, 99, 81, 2, 12], [0, 1, 7, 9, 22, 19, 81, 2, 1], [10, 20, 7, 9, 32, 9, 8, 2, 2]], [[3, 0, 0, 0, 5, 18, 6, 2, 1], [1, 17, 19, 7, 5, 1, 23, 9, 0]]]

bias_list = [ [0.5, 1, 0.2], [1, 0.1] ]

saidas = rede(entradas, pesos_list, bias_list, sigmoid)

def decisao_final(saidas):
    return saidas.index(max(saidas))

indice = decisao_final(saidas)

if indice > 0:
    resposta = "sim"
else:
    resposta = "não"

print(f"    A respectiva resposta é: {resposta}")