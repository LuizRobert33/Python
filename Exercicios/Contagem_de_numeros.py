contador = 0
while True:
    N = int(input("Digite o numero (digite 0 para interromper o programa): "))
    contador += N
    if N == 0:
        break
print(contador)    