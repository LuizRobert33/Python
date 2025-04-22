import os

lista = []

while True:
    print("Selecione uma opção")
    opcao = input("[i] inserir [a] apagar [l] listar [s] sair: ")

    if opcao == "i":
        os.system("cls")
        valor = input("Valor: ")
        lista.append(valor)
    elif opcao =="a":
        indice_str = input(
            "Escolha o indice para apagar  "
        )

        indice = int(indice_str)
        del lista[indice]
    elif opcao =="l":
        os.system("cls")

        if len(lista) == 0:
            print("Nada para listar ")
        for i, valor in enumerate(lista):
            print(i,valor)    
    elif opcao =="s":
        print("Programa Encerrado")
        break    
    else:
        print("Digite uma opção valida")            

    