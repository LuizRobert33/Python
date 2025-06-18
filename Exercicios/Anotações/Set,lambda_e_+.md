# Anotações de Python

# ==============================
# set (conjuntos)
# ==============================

# Estrutura de dados que não permite valores duplicados.
# Útil para remover duplicatas e realizar operações de conjuntos como união, interseção e diferença.

# Criando um set a partir de uma lista
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

vou por o titulo de alguns videos: set, função lamda + list.sort e sortedm funções lambda complexas(para entedimentos) , empacotamente e desempacotamente de dicionarios + *args e **kwargs