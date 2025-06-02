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