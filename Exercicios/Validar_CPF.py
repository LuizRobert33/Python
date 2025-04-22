
N = 1
lista = []

while N <= 11: 
    try:
        numero = int(input(f"Digite o {N}º número do CPF (0 a 9): "))
        if 0 <= numero <= 9:
            lista.append(numero)
            N += 1
        else:
            print("Digite apenas números entre 0 e 9.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Pegando os 9 primeiros dígitos
novo_numero = lista[:9]


NV = 0
M = 10
multiplicacao = []

while NV < len(novo_numero):
    resultado = novo_numero[NV] * M  
    multiplicacao.append(resultado)
    NV += 1
    M -= 1

print("Multiplicações:", multiplicacao)
print("Soma:", sum(multiplicacao))
