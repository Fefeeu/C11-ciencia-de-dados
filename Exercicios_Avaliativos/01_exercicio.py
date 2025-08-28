# %%
import numpy as np

dt = np.loadtxt("paises.csv",
                delimiter=";",
                dtype=str,
                encoding='utf-8')

# ================ EXERCICIO 1 ================
dt_sliced = dt[:,[0, 1, 2, 3]]

print(dt_sliced)

# ================ EXERCICIO 2 ================

regioes = np.unique(dt[1:,1])

print(f"\n\nSão {len(regioes)} regiões, dentre elas: {regioes}")

# ================ EXERCICIO 3 ================

quantidade = len(dt[np.char.find(dt[:,1], "NORTHERN AMERICA") >= 0][:,0])
print(f"\n\nSão {quantidade} Paises")

# ================ EXERCICIO 4 ================

alfabetizacao = dt[1:,9].astype(float).mean()

print(f"\n\nA porcentagem da população do planeta que é Alfabetizada é: {alfabetizacao:.4}%")

# ================ EXERCICIO 5 ================

america_sul_caribe = (np.char.find(dt[:,1], "LATIN AMER. & CARIB") >= 0) 

maior_renda = dt[:,8][america_sul_caribe].astype(float).max()

pais_maior_renda = dt[1:][dt[1:,8].astype(float) == maior_renda]

print(f"\n\nO pais com maior renda per capita é {pais_maior_renda[0,0]} com uma renda de {maior_renda}")