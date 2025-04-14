Nome = input("Digite seu nome: ")
Peso = float(input("Digite seu peso em kg: "))
Altura = float(input("Digite sua altura em metros: "))

IMC = Peso / (Altura * Altura)

if IMC < 18.5:
    print("Magreza")
elif 18.5 <= IMC <= 24.9:
    print("Normal")
elif 24.9 < IMC <= 29.9:
    print("Sobrepeso")
elif 29.9 < IMC <= 34.9:
    print("Obesidade grau I")
else:
    print("Obesidade grau II ou superior")

print(f"{Nome}, seu IMC é {IMC:.2f}")
