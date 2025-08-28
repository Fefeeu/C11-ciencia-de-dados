# %%
import numpy as np

dt = np.loadtxt("data/paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

quantidade = len(dt[np.char.find(dt[:,1], "NORTHERN AMERICA") >= 0][:,0])
print(f"São {quantidade} Paises")