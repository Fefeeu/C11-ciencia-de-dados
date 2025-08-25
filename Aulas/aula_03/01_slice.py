# %%
import numpy as np

mtz = np.arange(1, 10, 1).reshape(3, 3)
print(mtz)

# pegando linhas:
print(mtz[2])

# pegando colunas
print(mtz[:,1].reshape(3,1))

# %%
# pegando mais de uma coluna
print(mtz[:,1:])