import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Leitura dos dados
df = pd.read_csv('dados_temperatura.csv')

# Separando variáveis
X = df[['Mes']]  # Variável independente (mês)
y = df['Temperatura']  # Variável dependente (temperatura)

# Criando o modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Fazendo previsões para o mês 13
previsao = modelo.predict([[13]])
print(f'A previsão para o mês 13 é: {previsao[0]:.2f}°C')

# Visualizando a reta de regressão
plt.scatter(X, y, color='blue')
plt.plot(X, modelo.predict(X), color='red')
plt.xlabel('Mês')
plt.ylabel('Temperatura (°C)')
plt.show()
