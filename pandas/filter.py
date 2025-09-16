# %%
import pandas as pd
import numpy as np

# %% 
data = {
    "Fruit": ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "Color": ["Red", "Yellow", "Red", "Brown", "Black"],
    "Quantity": [10, 15, 30, 25, 12],
    "Price_per_item": [0.50, 0.25, 0.75, 1.00, 1.50],
    "Total_price": [5.00, 3.75, 22.50, 25.00, 18.00],
    "isAvailable": [True, True, True, True, True]
}

# %%
df_transformed = pd.DataFrame(data)
df_transformed