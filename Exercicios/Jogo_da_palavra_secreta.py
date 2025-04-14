palavra_secreta = "Futebol"
letras_acertadas = ""

while True:
    Letra = input("Digite uma letra: ")

    if len(Letra) > 1:
        print("ERRO.... digite apenas uma letra: ")
        continue

    if Letra in palavra_secreta:
        letras_acertadas += Letra 

    if Letra in palavra_secreta:
        if letras_acertadas in letras_acertadas:
            print(letras_acertadas)
        else:
            print("*")    