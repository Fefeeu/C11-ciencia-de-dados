# %%
import numpy as np

dt = np.loadtxt("data/paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

regioes = np.unique(dt[1:,1])

print(f"São {len(regioes)} regiões, dentre elas: {regioes}")