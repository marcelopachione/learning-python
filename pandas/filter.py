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

# %%
df_transformed = pd.DataFrame(data)
df_transformed

# %%
week_column = df_transformed['Week']
# week_column
# week_column.shape

# %%
subset = df_transformed[['Week', 'Red_Flag', 'Fruit', 'Color']]
subset

# %%
df_transformed.loc[[0, 2], ['Week', 'Red_Flag', 'Fruit']]

# %%
df_transformed_high_quantity = df_transformed[df_transformed['Quantity'] > 15]
df_transformed_high_quantity

# %%
df_transformed_low_quantity = df_transformed[df_transformed['Quantity'] < 15]
df_transformed_low_quantity

# %%
specific_red = df_transformed[
    (df_transformed['Red_Flag'] ==  True) | 
    (df_transformed["Quantity"] > 15)
]
specific_red

specific_fruit = df_transformed[
    (df_transformed['Fruit'].isin(['Apple', 'Cherry']))
]
specific_fruit