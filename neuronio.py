def neuronio(entradas, pesos_neuronio, bia, ativacoes):
    resultado = bia
    for entrada, pesos in zip(entradas, pesos_neuronio):
        resultado += entrada*pesos
    return ativacoes(resultado)