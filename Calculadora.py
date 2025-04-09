contador = 1
soma = 0
produto = 1
subtracao = None
divisao = None
tem_numeros = False

while True:
    entrada = input(f"Digite o {contador}º número ou '=' para calcular: ")
    
    if entrada == "=":
        break
    
    try:
        numero = float(entrada)
        tem_numeros = True
        soma += numero
        produto *= numero
        
        if subtracao is None:
            subtracao = numero
        else:
            subtracao -= numero

        if divisao is None:
            divisao = numero
        else:
            if numero != 0:
                divisao /= numero
            else:
                print("Aviso: Divisão por zero ignorada.")
        
        contador += 1

    except ValueError:
        print("Entrada inválida. Digite um número válido ou '=' para calcular.")

if tem_numeros:
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    
    if operacao == "+":
        print("Resultado da soma:", soma)
    elif operacao == "-":
        print("Resultado da subtração:", subtracao)
    elif operacao == "*":
        print("Resultado do produto:", produto)
    elif operacao == "/":
        print("Resultado da divisão:", divisao)
    else:
        print("Operação inválida.")
else:
    print("Nenhum número foi digitado.")
