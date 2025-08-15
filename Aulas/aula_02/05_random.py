# %%
import numpy as np

arr = np.random.randint(1, 101, 10)
print(arr)

# %%
np.random.seed(10)
mesmo_numero = np.random.randint(1, 101, 10)
print(mesmo_numero)