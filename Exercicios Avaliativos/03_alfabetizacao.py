# %%
import numpy as np

dt = np.loadtxt("data/paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

alfabetizacao = dt[1:,9].astype(float).mean()

print(f"A porcentagem da população do planeta que é Alfabetizada é: {alfabetizacao:.4}%")