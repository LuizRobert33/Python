# Dicionários em Python

Dicionários são estruturas de dados que armazenam pares de chave-valor. Eles são mutáveis, dinâmicos e não permitem chaves duplicadas.

## Criando um dicionário

```python
meu_dict = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
```

## Acessando valores

```python
print(meu_dict["nome"])  # Saída: Ana
```

## Adicionando e modificando valores

```python
meu_dict["idade"] = 26  # Modifica o valor existente
meu_dict["profissão"] = "Engenheira"  # Adiciona nova chave
```

## Removendo itens

```python
del meu_dict["cidade"]  # Remove a chave 'cidade'
```

## Métodos úteis

- `keys()`: retorna as chaves
- `values()`: retorna os valores
- `items()`: retorna pares (chave, valor)

```python
for chave, valor in meu_dict.items():
    print(chave, valor)
```

## Verificando se uma chave existe

```python
if "nome" in meu_dict:
    print("Chave encontrada!")
```

## Dicionários aninhados

```python
alunos = {
    "aluno1": {"nome": "Ana", "idade": 25},
    "aluno2": {"nome": "João", "idade": 22}
}
```

## Compreensão de dicionários

```python
quadrados = {x: x*x for x in range(5)}
print(quadrados)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Referências

- [Documentação oficial](https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries)

### Exemplo:
```python
""" Crie um dicionário chamado pessoa com as seguintes informações:

nome: "Carlos"
idade: 30
cidade: "Belo Horizonte"
Depois, adicione uma nova chave chamada "profissão" com o valor "Médico".
Por fim, remova a chave "cidade" do dicionário
"""
dicionario = {"nome": "Calors", "idade": 30, "cidade": "BH"}
pessoa["profissão"] = "Médico"
del pessoa["cidade"]
print(pessoa) 
```

# Atividade de Sistema de Pergunta e resposta
```python
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
```