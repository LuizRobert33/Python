try:
    Hora = int(input("Digite hora em inteiros: "))


    if Hora >= 0 and Hora <= 11:
        print("Bom dia")
    elif Hora >= 12 and Hora <= 17:
        print("Boa tarde")
    elif Hora >= 18 and Hora <= 23:
        print("Boa noite")
    else:
        print("Digite uma hora valida entre 0 e 23")    
except:
    print("Digite uma hora valida")                