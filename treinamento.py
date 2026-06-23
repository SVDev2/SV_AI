def treinar(entradas, pesos, bias, esperado,lr, ativacoes, derivada):
    
    soma = bias
    
    for x, y in zip(entradas, pesos):
        soma += x * y
        
    saida = ativacoes(soma)
    
    erro = esperado - saida
    
    gradiente = erro * derivada(soma)
    
    for i in range(min(len(pesos), len(entradas))):
        pesos[i] += gradiente * entradas[i] * lr
        
    bias += gradiente * lr
    
    return saida, pesos, bias  
    
    