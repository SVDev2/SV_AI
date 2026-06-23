import math

def degrau(resultado):
    if resultado > 0:
        return 1
    else:
        return 0

def sigmoid(resultado):
    return 1 / (1 + math.exp(-resultado))
    
def sigmoid_derivada(x):
    s = sigmoid(x)
    return s * (1-s)