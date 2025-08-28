# %%
import numpy as np

dt = np.loadtxt("data/paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

dt_sliced = dt[:,[0, 1, 2, 3]]

print(dt_sliced)