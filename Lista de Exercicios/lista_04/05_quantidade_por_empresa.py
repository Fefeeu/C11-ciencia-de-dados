# %%
import numpy as np

df = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")

empresas = np.unique_counts(df[1:,1])

for empresa, quantidade in zip(empresas[0], empresas[1]):
    print("A empresa:", empresa, "Fez:", quantidade, "missões")