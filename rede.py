from camada import camada

def rede(entradas, pesos_list, bias_list, ativacoes):
    
    historico = []
    
    for pesos, bias in zip(pesos_list, bias_list):
        entradas = camada(entradas, pesos, bias, ativacoes)
        entradas_m = entradas["saidas"]
        historico.append(entradas_m)
    return entradas, historico