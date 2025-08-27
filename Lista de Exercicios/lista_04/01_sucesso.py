# %%
import numpy as np

df = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")

porcentagem_sucesso = len(df[df[:,-1] == "Success"]) / (len(df)-1)
porcentagem_sucesso *= 100
print(f"Porcentagem de Sucesso: {np.round(porcentagem_sucesso, 2)}%")