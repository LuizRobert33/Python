nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if nome and idade:
    print(f"Nome: {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Idade: {idade} ")

    if '' in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contem Espaços") 
    
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:
    print("Você Deixou algum campo vazio")