# %%
import numpy as np

dt = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")
print(dt[0, :]) # colunas

# %%
coluna_custo = dt[1:, 6].astype(float)
print(coluna_custo[coluna_custo!=0].mean())

# %%
missoes_spaceX = dt[:, 1] == "SpaceX"
missoes_spaceX
# %%
valor_mais_caro = dt[missoes_spaceX][:, 6].astype(float).max()
valor_mais_caro
# %%
missoes_mais_caras = dt[1:, 6].astype(float) == valor_mais_caro
missoes_mais_caras = np.append(np.array([False]), missoes_mais_caras)
# %%
dt[missoes_mais_caras and dt[dt[:, 1] == "SpaceX"]]
# %%
