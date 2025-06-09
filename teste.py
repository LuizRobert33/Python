perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

pontuacao = 0  # Para contar respostas corretas

# Loop para cada pergunta no quiz
for pergunta in perguntas:
    print( pergunta['Pergunta'])  # Mostra a pergunta
    print()
    
    # Mostra as opções
    for i, opcao in enumerate(pergunta['Opções']):
        print(f"{i + 1}. {opcao}")
    
    # Recebe a resposta do usuário
    resposta_usuario = input("\nEscolha uma opção (1-4): ")
    
    # Converte a resposta do usuário para o valor correspondente na lista
    resposta_escolhida = pergunta['Opções'][int(resposta_usuario) - 1]
    
    # Verifica se a resposta está correta
    if resposta_escolhida == pergunta['Resposta']:
        print("Resposta correta!")
        pontuacao += 1
    else:
        print(f"Resposta incorreta. A resposta correta era: {pergunta['Resposta']}")

# Mostra o resultado final
print(f"\nVocê acertou {pontuacao} de {len(perguntas)} perguntas!")
