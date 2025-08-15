# %%
import numpy as np

arr = np.random.randint(1, 10, 20)
print(arr)
print(np.unique(arr))
print(np.unique(arr, return_counts=True))
