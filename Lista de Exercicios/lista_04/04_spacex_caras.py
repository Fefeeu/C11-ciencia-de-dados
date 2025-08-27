# %%
import numpy as np

df = np.loadtxt("data/space.csv", 
                delimiter=";", 
                dtype=str,
                encoding="utf-8")

valores_spaceX = df[1:,-2][df[1:,1] == "SpaceX"].astype(float)
missoes = df[1:,4][df[1:,1] == "SpaceX"][valores_spaceX == valores_spaceX.max()] 

print("Missões mais caras da SpaceX:", missoes)