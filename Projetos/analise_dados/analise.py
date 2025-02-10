import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('dados.csv')

# Exibição dos dados
print("Dados lidos do CSV:")
print(df)

# Manipulação de dados
media_idade = df['Idade'].mean()
print(f"\nA média de idade é: {media_idade}")

# Filtrando dados
filtrados = df[df['Idade'] > 28]
print("\nPessoas com mais de 28 anos:")
print(filtrados)
