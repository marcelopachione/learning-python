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

fruit_extra_details_data = {
    'Fruit': ['Apple', 'Banana', 'Mango', 'Date', 'Grape'],
    'Origin_Country': ['USA', 'Ecuador', 'India', 'Egypt', 'Italy'],
    'Is_Organic': [False, True, True, False, True],
    'Vitamin_C_mg': [5.0, 10.3, 36.4, 2.0, 6.0]
}

df = pd.DataFrame(data)
df_fruit = pd.DataFrame(fruit_extra_details_data)

# %%
df_inner_join = pd.merge(df, df_fruit, on='Fruit', how='inner')
df_inner_join

# %%
df_left_join = pd.merge(df, df_fruit, on='Fruit', how='left')
df_left_join

# %%
df_outer_join = pd.merge(df, df_fruit, on='Fruit', how='outer')
df_outer_join

fruit_details_alt = {
    'Fruit_Name': ['Apple', 'Banana', 'Mango'],
    'Supplier_ID': ['S1', 'S2', 'S1']
}

# %%
df_fruit_details = pd.DataFrame(fruit_details_alt)
df_fruit_details

# %%
df_merge = pd.merge(
    df,
    df_fruit_details,
    left_on='Fruit',
    right_on='Fruit_Name',
    how='left'
)
df_merge