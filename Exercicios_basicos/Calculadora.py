
print("Digite números um por um. Digite '=' para calcular.")

soma = 0
produto = 1
primeiro = True
subtracao = 0
divisao = 0
contador = 0

while True:
    entrada = input("Digite um número ou '=' para calcular: ")
    
    if entrada == "=":
        break

    numero = float(entrada)
    contador += 1

    soma += numero
    produto *= numero

    if contador == 1:
        subtracao = numero
        divisao = numero
    else:
        subtracao -= numero
        divisao /= numero

operacao = input("Qual operação? (+, -, *, /): ")

if operacao == "+":
    print("Resultado da soma:", soma)
elif operacao == "-":
    print("Resultado da subtração:", subtracao)
elif operacao == "*":
    print("Resultado da multiplicação:", produto)
elif operacao == "/":
    print("Resultado da divisão:", divisao)
else:
    print("Operação inválida.")
