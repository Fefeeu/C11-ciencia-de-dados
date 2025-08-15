# %%
import numpy as np
#   X   Agua    Luz     Net
#   JUN 50      10      100
#   FEV 60      30      100
#   MAR 70      80      100

matriz_pagamento = np.array([50, 10, 100, 60, 30, 100, 70, 80, 100])
matriz_pagamento = matriz_pagamento.reshape(3,3)
print(matriz_pagamento)
print()
print(matriz_pagamento.sum(axis=0)) #colunas
print(matriz_pagamento.sum(axis=1)) #linhas

# %%
print("Valor da Net: ", matriz_pagamento.sum(axis=0)[2])