# Funções em Python
## Sintaxe básica

```python
def nome_da_funcao(parâmetros):
    # bloco de código
    return resultado
# exemplo Simples    
def saudacao():
    print("Olá, bem-vindo!")

# Função com parâmetros
def soma(a, b):
    resultado = a + b
    return resultado
print(soma(5,3)) # sainda: 8

# Parâmetros opcionais (com valor padrão)
def saudacao(nome="usuário"):
    print(f"Olá, {nome}!")
saudacao() # Olá, usuário
saudacao("Maria") # Olá, Maria

# Retorna valores
def quadrado(numero):
    return numero ** 2
resultado = quadrado(4)
print(resultado)  # Saída: 16


# Função com múltiplos retornos
def operacoes(a, b):
    soma = a + b
    sub = a - b
    return soma, sub
x, y = operacoes(5, 3)
print(x)  # 8
print(y)  # 2

# Função com argumentos infinitos
## *args  → paranetros posicionais
def soma(*numeros):
    return sum(numeros)

print(soma(1, 2, 3, 4))  # 10

## **kwargs → parâmetros nomeados
def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Ana", idade=25)
```
