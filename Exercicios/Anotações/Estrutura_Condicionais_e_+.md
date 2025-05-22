# Estrutura Concidiconal
## Sintaxe
```python
if condição:
    # código executado se condição for verdadeira
else:
    # código se condição for falsa

# Exemplo:
    idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```
```python
#if,else, if

if condição1:
    # código se condição1 for verdadeira
elif condição2:
    # código se condição2 for verdadeira
else:
    # código se nenhuma condição anterior for verdadeira

Exemplo:
idade = 18

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
else:
    print("Precisa melhorar")
```
# Operadores Logicos:

and → Retorna True se todas as condições forem verdadeiras.

or → Retorna True se pelo menos uma das condições for verdadeira.

not → Inverte o valor lógico da condição (True vira False e vice-versa).

```Python
# Exemplos:
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
else:
    print("Não pode dirigir")
############

choveu = False
sol = True

if choveu or sol:
    print("Levar guarda-chuva ou protetor solar")
############

ativo = False

if not ativo:
    print("Usuário inativo")
```
# Laços de Repetições

## Laço `for`

### Usado para percorrer sequências (listas, strings, ranges, etc.).

```python
for variavel in sequencia:
    # bloco de código

## Exemplo com range()
for i in range(5):
    print(i)
# Saída: 0, 1, 2, 3, 4

# Exemplo percorrendo lista  
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

# Exemplo percorrendo string
for letra in "Python":
    print(letra)
```
## Laço While
```python
while condição:
    # bloco de código
## Exemplo
contador = 0

while contador < 5:
    print(contador)
    contador += 1
###############

Comandos de controle dentro dos laços
break → Interrompe o laço e sai dele.

continue → Interrompe a iteração atual e vai para a próxima.

Exemplo com break:

for i in range(10):
    if i == 5:
        break
    print(i)
# Saída: 0, 1, 2, 3, 4
Exemplo com continue:

for i in range(5):
    if i == 2:
        continue
    print(i)
# Saída: 0, 1, 3, 4   
```
### Observação:
O for em Python é mais usado para percorrer coleções ou sequências.

O while é usado quando não sabemos exatamente quantas repetições serão feitas, mas sabemos a condição de parada.

Sempre tomar cuidado com o while para não criar loops infinitos.

# Flags: `is`, `is not` e `None` em Python

## `None`
- Representa a ausência de valor ou um valor nulo em Python.
- Usado para indicar que uma variável está vazia ou sem valor atribuído.

### Exemplo:
```python
valor = None

if valor is None:
    print("Sem valor")
else:
    print("Tem valor")
```
is e is not<br>
O que são?<br>
São operadores de identidade, usados para comparar se dois objetos ocupam o mesmo espaço na memória.

Diferente de ==, que compara se os valores são iguais, is verifica se são exatamente o mesmo objeto.
## is → É o mesmo objeto?
```python
a = None

if a is None:
    print("É None")
```
## is not → Não é o mesmo objeto?
```python
a = 10

if a is not None:
    print("Tem valor")
```
Diferença entre is e ==
== compara se os valores são iguais.

### is compara se é o mesmo objeto na memória.

Exemplo prático:
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True (os valores são iguais)
print(a is b)   # False (não são o mesmo objeto na memória)
Quando usar is?
Para comparar com objetos únicos como None.

Para verificar identidade de objetos, não seus valores.

Correto:

if valor is None:
    print("Sem valor")
Errado:
python
Copiar
Editar
if valor == None:  # Funciona, mas não é a forma recomendada.
    print("Sem valor")
Resumo:
is → mesmo objeto na memória.

is not → objetos diferentes na memória.

None → ausência de valor.
```
