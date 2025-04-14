palavra_secreta = "futebol"
letras_acertadas = ""

while True:
    letra = input("Digite uma letra: ").lower()

    if len(letra) > 1:
        print("ERRO... digite apenas uma letra.")
        continue

    if letra in palavra_secreta and letra not in letras_acertadas:
        letras_acertadas += letra

    palavra_formada = ""
    for l in palavra_secreta:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += "*"

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print("Parabéns! Você descobriu a palavra secreta.")
        break
