try:
    N = int(input("Digite um número inteiro: "))

    if N % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

except ValueError:
    print("Erro: você precisa digitar um número inteiro válido.")
