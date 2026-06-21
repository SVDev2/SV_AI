from camada import camada

def rede(entradas, pesos_list, bias_list, ativacoes):
    for pesos, bias in zip(pesos_list, bias_list):
        entradas = camada(entradas, pesos, bias, ativacoes)
    return entradas