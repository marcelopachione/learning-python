# Exploracao 

# Import pandas
# %%
import pandas as pd

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
# display(df)
df.head(5)
# df.tail(2)
# df.info()
# df.dtypes
# df.shape
# df.index

# %%
# O comando calcula automaticamente o valor total (quantidade × preço unitário) para cada linha e armazena em Total_price.
df['Total_price'] = df['Quantity'] * df['Price_per_item']
df

# %%
# Cria (ou sobrescreve) a coluna Available em df, atribuindo o valor True para todas as linhas dessa coluna.
df['Available'] = True
df

# %%
df = df.rename(columns={
    'Available': 'isAvailable'
})
df

# %%
# Seleciona a linha de índice (rótulo) 2 do DataFrame e retorna essa linha como uma Series com os valores de cada coluna.
df.loc[2]

# %%
# Seleciona na linha de índice 2 apenas as colunas 'Fruit' e 'Total_price', retornando seus valores (como uma Series com esses dois campos).
df.loc[2, ['Fruit', 'Total_price']]

# %%
# Seleciona as linhas de índice 0 até 2 (inclusive) e, dessas linhas, apenas as colunas 'Fruit' e 'Total_price', retornando um DataFrame com esse recorte.
df.loc[0:2, ['Fruit', 'Total_price']]

# %%
# Seleciona o valor que está na linha de posição 0 e coluna de posição 1 (baseado em posição numérica), retornando um único valor (escalar).
df.iloc[0,1]

# %%
# Filtra um subconjunto de df, pegando linhas 1–3 e colunas 0 e 2, usando posições numéricas.
df.iloc[1:4, [0,2]]