# %%
import numpy as np

# CRIANDO UM numpy ARRAY NO HARDCODE
# obs.: o numpy.array() aceita somente valores do mesmo tipo
array_exemplo = np.array([10, 20, 30, 40, "teste"])
print(array_exemplo)
print(type(array_exemplo))
print()

array_numpy = np.array([10, 20, 30, 40, 50])
print(array_numpy)
print(type(array_numpy))
print()

matriz_numpy_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print(matriz_numpy_2d)

# %%
# FUNCOES PARA ESTRUTURAR numpy arrays

array_de_uns = np.ones(10)
array_de_zeros = np.zeros(10)
print(array_de_uns)
print(array_de_zeros)
print()

# np.zeros(N)
# obs.: Obrigatoriamente -> X*Y = N
print(array_de_zeros.reshape(5,2))
print()

# %%
# CRIANDO UMA MATRIZ DE FORMA DIRETA
matriz_de_zeros = np.zeros([10, 5])
print(matriz_de_zeros)
print()

# %%
array_numpy = np.arange(10, 31, 3) # de 10 a 30 pulando de 3 em 3
print(array_numpy)
print()

# %%
array_numpy = np.arange(10, 101, 10)
print(array_numpy)

# menor valor
print(array_numpy.min(), "na posicao", array_numpy.argmin())

# maior valor
print(array_numpy.max(), "na posicao", array_numpy.argmax())

# media
print(array_numpy.mean())
print()

# %%
