# %%
import numpy as np

arr1 = np.arange(1, 10, 1)
arr2 = np.arange(9, 0, -1)

print(arr1)
print(arr2)
print()

# %%
# SOMA DA POSICAO DOS DOIS ARRAYS
print(arr1 + arr2)
print()

# %%
arr1_2 = np.concatenate([arr1, arr2])
print(arr1_2)