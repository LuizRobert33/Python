import math
def Multi(*numeros):
    print(numeros)  # Mostra a tupla inteira
    return math.prod(numeros)

print(Multi(1, 2, 5))  
