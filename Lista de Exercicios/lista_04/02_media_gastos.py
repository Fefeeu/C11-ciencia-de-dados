# %%
import numpy as np

df = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")

filtro = df[1:,-2].astype(float) > 0

custo_medio = df[1:,-2][filtro].astype(float).sum()/(len(df[1:][filtro])-1)

print(f"Preço Médio das Missões: {custo_medio:.5}R$")