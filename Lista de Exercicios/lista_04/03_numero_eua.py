# %%
import numpy as np

df = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")



numero_nos_eua = len(df[1:,2][np.char.find(df[1:,2], "USA") >= 0])

print("Numero de missões nos Estados Unidos:", numero_nos_eua)