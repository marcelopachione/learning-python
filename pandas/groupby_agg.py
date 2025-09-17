# %%
import pandas as pd
import numpy as np

# %% 
data = {
    "Fruit":      ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "Color":      ["Red", "Unknown", "Red", "Brown", "Black"],
    "Quantity":   [10.00, 15.00, 30.00, 16.75, 12.00],
    "Price_per_item": [0.50, 0.25, 0.75, 1.00, 1.50],
    "Total_Price":    [0.00, 3.75, 22.50, 25.00, 18.00],
    "In_Stock":   [True, True, True, True, True],
    "Week":       [5, 6, 1, 23, 18],
    "Red_Flag":   [True, False, True, False, False]
}

df = pd.DataFrame(data)
df

# %%
qtde_per_color = df.groupby('Color')['Quantity'].sum()
qtde_per_color

# %%
media_per_color = df.groupby('Color')['Quantity'].mean()
media_per_color

# %%
count_red_flag = df.groupby('Red_Flag')['Fruit'].count()
count_red_flag

# %%
df_agg = df.groupby('Color').agg(
    total_quantity = ('Quantity', 'sum'),
    avg_quantity = ('Quantity', 'mean'),
    count_red_falg = ('Red_Flag', 'count'),
    max_per_item= ('Price_per_item', 'max'),
    min_week= ('Week', 'min'),
)
df_agg