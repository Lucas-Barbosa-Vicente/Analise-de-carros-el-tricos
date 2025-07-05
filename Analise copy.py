<<<<<<< HEAD


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('C:/Users/Lucas/OneDrive/Área de Trabalho\Analise de carros eletricos/Dados_veiculos_eletricos.csv')

df.head()
print(df.info())
print(df.columns)

plt.figure(figsize=(10, 5))
df['make'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Marcas com Mais Veículos Elétricos')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
df.groupby('ev_type')['electric_range'].mean().sort_values().plot(kind='barh', color='lightgreen')
plt.title('Autonomia Média por Tipo de Veículo')
plt.xlabel('Autonomia Média (milhas)')
plt.ylabel('Tipo de Veículo')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
df['model_year'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title('Evolução de Registros de Veículos Elétricos por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Registros')
plt.grid(True)
plt.tight_layout()
plt.show()

df['Autonomia_por_Preco'] = df['electric_range'] / df['base_msrp']

modelos_populares = df['model'].value_counts()
modelos_filtrados = modelos_populares[modelos_populares > 100].index
df_filtrado = df[df['model'].isin(modelos_filtrados)]

eficiencia_modelo = df_filtrado.groupby('model')['Autonomia_por_Preco'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
eficiencia_modelo.plot(kind='bar', color='orange')
plt.title('Top 10 Modelos Mais Eficientes (Autonomia por Preço)')
plt.xlabel('Modelo')
plt.ylabel('Eficiência (mi/USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_autonomia = df[['model', 'electric_range']].groupby('model').mean().sort_values(by='electric_range', ascending=False).head(10)
estado_contagem = df['state'].value_counts().reset_index()
estado_contagem.columns = ['state', 'Quantidade']

cafv = df['cafv_type'].value_counts()
utility = df['electric_utility'].value_counts().head(10)
df.to_csv('veiculos_eletricos_limpo.csv', index=False)
top_autonomia.to_csv('top_autonomia_modelos.csv')
estado_contagem.to_csv('distribuicao_estados.csv')

import requests
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
response = requests.get(url)
with open("dados_carros.csv", "wb") as file:
    file.write(response.content)
df = pd.read_csv("dados_carros.csv")
print(df.head())

df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.dropna()
print("Dados processados com sucesso!")

import matplotlib.pyplot as plt
modelos_populares = df['model'].value_counts().head(10)
plt.figure(figsize=(10,5))
modelos_populares.plot(kind='bar', color='skyblue')
plt.xlabel("Modelo")
plt.ylabel("Quantidade")
plt.title("Top 10 Modelos de Veículos Elétricos")
plt.xticks(rotation=45)
plt.show()

import schedule
import time

def executar_analise():
    print("Baixando e analisando dados...")
    
schedule.every().day.at("09:00").do(executar_analise)

while True:
    schedule.run_pending()
    time.sleep(60)  
=======


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('C:/Users/Lucas/OneDrive/Área de Trabalho\Analise de carros eletricos/Dados_veiculos_eletricos.csv')

df.head()
print(df.info())
print(df.columns)

plt.figure(figsize=(10, 5))
df['make'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Marcas com Mais Veículos Elétricos')
plt.xlabel('Marca')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
df.groupby('ev_type')['electric_range'].mean().sort_values().plot(kind='barh', color='lightgreen')
plt.title('Autonomia Média por Tipo de Veículo')
plt.xlabel('Autonomia Média (milhas)')
plt.ylabel('Tipo de Veículo')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
df['model_year'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title('Evolução de Registros de Veículos Elétricos por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Registros')
plt.grid(True)
plt.tight_layout()
plt.show()

df['Autonomia_por_Preco'] = df['electric_range'] / df['base_msrp']

modelos_populares = df['model'].value_counts()
modelos_filtrados = modelos_populares[modelos_populares > 100].index
df_filtrado = df[df['model'].isin(modelos_filtrados)]

eficiencia_modelo = df_filtrado.groupby('model')['Autonomia_por_Preco'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 5))
eficiencia_modelo.plot(kind='bar', color='orange')
plt.title('Top 10 Modelos Mais Eficientes (Autonomia por Preço)')
plt.xlabel('Modelo')
plt.ylabel('Eficiência (mi/USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

top_autonomia = df[['model', 'electric_range']].groupby('model').mean().sort_values(by='electric_range', ascending=False).head(10)
estado_contagem = df['state'].value_counts().reset_index()
estado_contagem.columns = ['state', 'Quantidade']

cafv = df['cafv_type'].value_counts()
utility = df['electric_utility'].value_counts().head(10)
df.to_csv('veiculos_eletricos_limpo.csv', index=False)
top_autonomia.to_csv('top_autonomia_modelos.csv')
estado_contagem.to_csv('distribuicao_estados.csv')

import requests
url = "https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD"
response = requests.get(url)
with open("dados_carros.csv", "wb") as file:
    file.write(response.content)
df = pd.read_csv("dados_carros.csv")
print(df.head())

df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.dropna()
print("Dados processados com sucesso!")

import matplotlib.pyplot as plt
modelos_populares = df['model'].value_counts().head(10)
plt.figure(figsize=(10,5))
modelos_populares.plot(kind='bar', color='skyblue')
plt.xlabel("Modelo")
plt.ylabel("Quantidade")
plt.title("Top 10 Modelos de Veículos Elétricos")
plt.xticks(rotation=45)
plt.show()

import schedule
import time

def executar_analise():
    print("Baixando e analisando dados...")
    
schedule.every().day.at("09:00").do(executar_analise)

while True:
    schedule.run_pending()
    time.sleep(60)  
>>>>>>> 33bc1fac1743e241e01cd4e1916273f1035402a1
