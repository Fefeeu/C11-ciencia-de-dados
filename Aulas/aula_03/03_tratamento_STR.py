# %%
import numpy as np 

arr = np.array(["Goku", "Goten", "Gohan", "Trunks", "Bulma"])

print(arr)

# %%
print(np.char.find(arr, "n"))

# %%

filtro = np.char.find(arr, "n")>=0
print(arr[filtro])