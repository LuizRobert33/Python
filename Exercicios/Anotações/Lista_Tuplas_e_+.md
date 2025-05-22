# Listas, Tuplas e Tratamento de Erros em Python

---

##  Listas

- Estruturas mutáveis (podem ser alteradas).
- Armazenam uma sequência de elementos.

### Criando uma lista:
```python
frutas = ["maçã", "banana", "laranja"]
Operações básicas:

print(frutas[0])      # Acessa o primeiro item
frutas.append("uva")  # Adiciona no final
frutas.remove("maçã") # Remove um item
print(len(frutas))    # Tamanho da lista
Percorrendo uma lista:

for fruta in frutas:
    print(fruta)
```    
# Tuplas
Estruturas imutáveis (não podem ser alteradas depois de criadas).<br>
Usadas para dados que não devem ser modificados.

```python
# Criando uma tupla
cores = ("vermelho", "verde", "azul")
# Acessando elementos:
print(cores[0])  # vermelho

"""Observação:
Tuplas com um único elemento precisam de vírgula:
"""

exemplo = (10,)  # Isso é uma tupla
```
# Tratamento de Erros ---> Try, Excpet e Finally
### Capturar e tratar erros durante a execução
#### Estrutura Básica:
```python
try:
    # Código que pode gerar erro
except TipoDoErro:
    # Código executado se ocorrer esse erro
finally:
    # Código que sempre executa (com erro ou sem erro)

# Exemplo Simples
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except ValueError:
    print("Erro: Você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
finally:
    print("Operação finalizada.")
