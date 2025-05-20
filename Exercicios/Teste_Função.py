def Soma(a,b,c):
    print(a,b,c)
    return a + b + c

print(Soma(2,3,5))


def somar_tudo(*numeros):
    print(numeros)  # Mostra a tupla inteira
    return sum(numeros)

print(somar_tudo(1, 2, 3))  # 6
print(somar_tudo(10, 20))   # 30
