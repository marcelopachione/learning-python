# Transformacao 

# Import pandas
# %%
import pandas as pd
import numpy as np

# %%
# Carrega dict
data = {
    'Fruit': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'],
    'Color': ['Red', 'Yellow', 'Red', 'Brown', 'Black'],
    'Quantity': [10, 15, 30, 25, 12],
    'Price_per_item': [0.5, 0.25, 0.75, 1.0, 1.5]
}

# %%
# Cria DataFrame
df = pd.DataFrame(data)
df

# %%
# O comando calcula automaticamente o valor total (quantidade × preço unitário) para cada linha e armazena em Total_price.
df['Total_price'] = df['Quantity'] * df['Price_per_item']
df

# %%
# Cria (ou sobrescreve) a coluna Available em df, atribuindo o valor True para todas as linhas dessa coluna.
df['Available'] = True
df

# %%
# Cria uma cópia do DataFrame df chamada df_transfomed,
# depois substitui o valor da coluna 'Color' na linha de índice 1 por NaN (valor ausente),
# e exibe o DataFrame modificado.
df_transfomed = df.copy()
df_transfomed.loc[1, 'Color'] = np.nan
df_transfomed.loc[3, 'Quantity'] = np.nan
df_transfomed.loc[0, 'Total_price'] = np.nan
df_transfomed

# %%
# Retorna um DataFrame de valores booleanos,
# onde cada célula indica se o valor correspondente em df_transfomed é nulo/NaN (True) ou não nulo (False).
df_transfomed.isnull()

# %%
# Mostra, para cada coluna de df_transfomed, quantos valores nulos (NaN) existem,
# retornando uma Series com o nome da coluna e a contagem de nulos.
df_transfomed.isnull().sum()

# %%
# Substitui os valores NaN da coluna 'Color' de df_transfomed pela string 'Unknow'
# e atribui o resultado de volta à própria coluna, sem alterar outros lugares do DataFrame original.
df_transfomed['Color'] = df_transfomed['Color'].fillna('Unknown', inplace=False)
df_transfomed

# %% 
# Preenche os valores nulos (NaN) da coluna 'Quantity' com a média dos valores dessa mesma coluna,
# e grava o resultado de volta em df_transfomed['Quantity'].
df_transfomed['Quantity'] = df_transfomed['Quantity'].fillna(df_transfomed['Quantity'].mean(), inplace=False)
df
# %%
df_transfomed['Total_price'] = df_transfomed['Total_price'].fillna(0, inplace=False)
df_transfomed.isnull().sum()

# %%
df_transfomed

# %%
# Cria (ou sobrescreve) a coluna 'Days' em df_transfomed,
# atribuindo a lista ['5', '6', '1', '24', '18'] como valores das linhas,
df_transfomed['Days'] = ['5', '6', '1', '24', '18']
df_transfomed.dtypes

# %% 
# Converte os valores da coluna 'Days' em df_transfomed de string para inteiro (int), deixando todos os valores dessa coluna como números inteiros.
df_transfomed['Days'] = df_transfomed['Days'].astype(int)
df_transfomed.dtypes

# %%
#Cria (ou sobrescreve) a coluna isRed em df_transfomed, marcando True quando o valor da coluna Color é 'Red' e False caso contrário.
df_transfomed['isRed'] = (df_transfomed['Color'] == 'Red')
df_transfomed

# %%
# Cria uma cópia da primeira linha de df_transfomed (x),e depois concatena essa cópia ao final de df_transfomed,
# gerando um novo DataFrame df_transfomed_duplicates que contém todas as linhas originais + uma linha duplicada da primeira linha.
x = df_transfomed.iloc[[0]]
df_transfomed_duplicates = pd.concat([df_transfomed, x], ignore_index=True)
df_transfomed_duplicates

# %%
# Remove do DataFrame df_transfomed_duplicates as linhas duplicadas, mantendo apenas a primeira ocorrência de cada linha repetida.
df_transfomed_duplicates = df_transfomed_duplicates.drop_duplicates()
# df_transfomed_duplicates = df_transfomed_duplicates.drop_duplicates(keep='first')
# df_transfomed_duplicates = df_transfomed_duplicates.drop_duplicates(keep='last')
df_transfomed_duplicates