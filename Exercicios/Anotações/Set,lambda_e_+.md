# Anotações de Python

# ==============================
# set (conjuntos)
# ==============================

# Estrutura de dados que não permite valores duplicados.
# Útil para remover duplicatas e realizar operações de conjuntos como união, interseção e diferença.

# Criando um set a partir de uma lista
```python
numeros = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(numeros)
print(conjunto)  # saída: {1, 2, 3, 4, 5}

# Adicionar e remover itens
conjunto.add(6)
print(conjunto)  # {1, 2, 3, 4, 5, 6}

conjunto.remove(3)
print(conjunto)  # {1, 2, 4, 5, 6}

# Se tentar remover algo que não existe dá erro
# conjunto.remove(10)  # KeyError

# Para evitar erro, use discard
conjunto.discard(10)  # Não gera erro

# Operações entre conjuntos
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # união: {1, 2, 3, 4, 5}
print(a & b)  # interseção: {3}
print(a - b)  # diferença: {1, 2}
print(a ^ b)  # diferença simétrica: {1, 2, 4, 5}

# Verificar se é subconjunto ou superconjunto
print({1, 2}.issubset(a))  # True
print(a.issuperset({1, 2}))  # True
print(a.isdisjoint(b))  # False (pois compartilham o 3)

# Sets não são indexáveis
# print(conjunto[0])  # TypeError

# Mas podem ser convertidos para lista se precisar acessar por índice
lista = list(conjunto)
print(lista[0])
```

# ==============================
# Funções Lambda + list.sort() + sorted()
# ==============================
```python
# ✅ Lambda:
# São funções anônimas, ou seja, sem nome.
# Úteis para funções pequenas e rápidas.
# Sintaxe: lambda argumentos: expressão

# Exemplo básico:
soma = lambda x, y: x + y
print(soma(2, 3))  # saída: 5

# ==============================

# ✅ list.sort() e sorted():
# Ambos servem para ordenar coleções, mas possuem diferenças importantes.

# ➕ list.sort()
# - Método da lista.
# - Ordena a própria lista (modifica ela).
# - Não retorna uma nova lista, retorna None.

# ➕ sorted()
# - Função embutida (built-in).
# - Retorna uma nova lista ordenada.
# - Não altera a lista original.

# ==============================

# 🔥 Exemplos práticos:

numeros = [5, 2, 9, 1, 7]

# Usando sorted() (não altera a lista original)
ordenada = sorted(numeros)
print('Original:', numeros)        # [5, 2, 9, 1, 7]
print('Ordenada:', ordenada)       # [1, 2, 5, 7, 9]

# Usando list.sort() (altera a própria lista)
numeros.sort()
print('Depois do sort:', numeros)  # [1, 2, 5, 7, 9]

# ==============================

# 🔑 Ordenando com chave (key) usando lambda:

pessoas = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Bruno', 'idade': 20}
]

# Ordenar por idade (forma crescente)
ordenado_idade = sorted(pessoas, key=lambda pessoa: pessoa['idade'])
print(ordenado_idade)
# [{'nome': 'Bruno', 'idade': 20}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Carlos', 'idade': 30}]

# Ordenar por nome (ordem alfabética)
ordenado_nome = sorted(pessoas, key=lambda pessoa: pessoa['nome'])
print(ordenado_nome)
# [{'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 20}, {'nome': 'Carlos', 'idade': 30}]

# ==============================

# 🔄 Ordenação decrescente:
numeros = [5, 2, 9, 1, 7]
numeros.sort(reverse=True)
print('Decrescente:', numeros)  # [9, 7, 5, 2, 1]

# ==============================

# 🧠 Mais exemplos de lambda com outras funções:
# - map, filter, reduce (exemplos rápidos)

# Quadrado dos números usando map + lambda
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16]

# Filtrar números pares usando filter + lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]
```

# ==============================
# Funções Lambda Complexas (Para Entendimento)
# ==============================
```python
# ✅ Lembrando:
# Sintaxe -> lambda argumentos: expressão
# Só pode ter uma expressão (não pode usar if/else em blocos, apenas ternário)
# Não possui nome, a não ser que seja atribuída a uma variável.

# ==============================

# 🔥 Lambda com condicional (if ternário)
# Exemplo: Verificar se número é par ou ímpar

par_ou_impar = lambda x: 'Par' if x % 2 == 0 else 'Ímpar'
print(par_ou_impar(4))  # Par
print(par_ou_impar(5))  # Ímpar

# ==============================

# 🔥 Lambda dentro de sorted() com múltiplas chaves
# Ordenar por idade e, em caso de empate, pelo nome

pessoas = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Carlos', 'idade': 30},
    {'nome': 'Bruno', 'idade': 25},
    {'nome': 'Diana', 'idade': 20}
]

ordenado = sorted(pessoas, key=lambda p: (p['idade'], p['nome']))
print(ordenado)
# Saída ordenada por idade e depois por nome

# ==============================

# 🔥 Lambda com operações matemáticas mais complexas
# Calcular a fórmula de Bhaskara (retorna as duas raízes)

import math
bhaskara = lambda a, b, c: (
    (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a),
    (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
)
print(bhaskara(1, -3, 2))  # (2.0, 1.0)

# ==============================

# 🔥 Lambda aninhada (lambda que retorna outra lambda)
# Função que gera uma função de potência

potencia = lambda n: lambda x: x ** n
quadrado = potencia(2)
cubo = potencia(3)
print(quadrado(5))  # 25
print(cubo(2))      # 8

# ==============================

# 🔥 Lambda com filter + condição composta
# Filtrar números entre 10 e 50 que sejam pares

numeros = list(range(1, 100))
filtrados = list(filter(lambda x: 10 <= x <= 50 and x % 2 == 0, numeros))
print(filtrados)
# [10, 12, 14, ..., 50]

# ==============================

# 🔥 Lambda com reduce (necessário importar functools)
# Calcular o fatorial de um número

from functools import reduce

fatorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print(fatorial(5))  # 120

# ==============================

# 🔥 Lambda para criar formatadores de string
# Cria uma função que adiciona prefixo e sufixo

formatador = lambda prefixo, sufixo: lambda texto: f'{prefixo}{texto}{sufixo}'
colchetes = formatador('[', ']')
asteriscos = formatador('***', '***')

print(colchetes('Python'))    # [Python]
print(asteriscos('Curso'))    # ***Curso***

# ==============================

# ✅ Observação:
# Embora seja possível criar lambdas complexas, quando a lógica fica extensa, 
# a recomendação do Python é usar def para melhorar a legibilidade.
```