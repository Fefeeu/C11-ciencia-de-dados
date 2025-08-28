# %%
import numpy as np

dt = np.loadtxt("data/paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

maior_renda = dt[1:,8].astype(float).max()

pais_maior_renda = dt[1:][dt[1:,8].astype(float) == maior_renda]

print(f"O pais com maior renda per capita é {pais_maior_renda[0,0]} com uma renda de {maior_renda}")
