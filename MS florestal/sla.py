# Importa o módulo pandas
import pandas as pd

# Defina um dicionário contendo dados de Alunos
data = {
        'Nome': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Altura': [5.1, 6.2, 5.1, 5.2],
        'Qualificação': ['Msc', 'MA', 'Msc', 'Msc']
        }

# Converta o dicionário em DataFrame
df = pd.DataFrame(data)
# Defina um dicionário com os valores-chave de
# uma coluna existente e seus respectivos
# pares de valores como os valores para nossa nova coluna.
# Converta o dicionário em DataFrame
df.insert(3, "Idade", [21, 23, 24, 21], True)

print(df)

texto = "Olá, Python!"
tamanho = len(texto)
print("O comprimento da string é:", tamanho)
numeros = [1, 2, 3, 4, 5]
quantidade = len(numeros)
print("O número de elementos na lista é:", quantidade)

coordenadas = (10, 20, 30)
elementos = len(coordenadas)
print("O número de elementos na tupla é:", elementos)

dados = {'nome': 'Maria', 'idade': 25, 'cidade': 'Exemplo'}
chaves = len(dados)
print("O número de chaves no dicionário é:", chaves)