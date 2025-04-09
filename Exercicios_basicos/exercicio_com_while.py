Nome = "Luiz Roberto"

I = 0
novo_nome = ""
while I < len(Nome):
    letra = Nome[I]
    novo_nome += f"*{letra}"
    I  += 1

print(novo_nome)     