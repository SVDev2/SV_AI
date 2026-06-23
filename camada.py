from neuronio import neuronio

def camada(entradas, pesos, bias, ativacoes):
    saidas = []
    for pesos_neuronio, bia in zip(pesos, bias):
        resultado = neuronio(entradas, pesos_neuronio, bia, ativacoes)
        saidas.append(resultado)
    return {"entradas" : entradas, "saidas" : saidas}