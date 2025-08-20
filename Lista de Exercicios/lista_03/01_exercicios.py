# %%
import numpy as np
# %%

# ============= EXERCICIO 1 =============
array_1s = np.ones(8)
array_09 = np.random.randint(1, 10, 8)
soma_arrays = array_09 + array_1s

if soma_arrays.sum() >= 40:
    soma_arrays = soma_arrays.reshape(4, 2)
else:
    soma_arrays = soma_arrays.reshape(2, 4)
print("Exercicio 1:")
print(soma_arrays)

# ============= EXERCICIO 2 =============
array_0_51 = np.arange(0, 51, 2)
array_100_50 = np.arange(100, 50, -2)
array_concatenado = np.concatenate([array_0_51, array_100_50])

print("\n\nExercicio 2:")
print(np.sort(array_concatenado))

# ============= EXERCICIO 3 =============
campo_minado = np.zeros(4).reshape(2, 2)
bomba = np.random.randint(0, 2, 2)

campo_minado[bomba[0]][bomba[1]] = 1

print("\n\nExercicio 3:")
while campo_minado.sum() != 7:
    print(campo_minado)
    posicao = int(input("Linha:")), int(input("Coluna:"))
    
    if campo_minado[posicao] == 1:
        print("Game Over! :( Try Again!")
        break
    campo_minado[posicao] = 2
    
else:
    print("Congratulations! You beat the game! :)")
    
# ============= EXERCICIO 4 =============
C = 10
L = 5

matriz_qualquer = np.matrix([[0]*C for i in range(L)])
linhas, colunas = matriz_qualquer.shape

if (linhas * colunas)%2 == 0:
    resposta = "pode virar uma matriz unidimencional com PAR elementos"
else:
    resposta = "pode virar uma matriz unidimencional com IMPAR elementos"
print("\n\nExercicio 4:")
print(resposta)

# ============= EXERCICIO 4 =============
np.random.seed(10)
matriz_4x4 = np.random.randint(1, 51, size=(4, 4))

media_linhas = matriz_4x4.mean(axis=1)
media_colunas = matriz_4x4.mean(axis=0)

for i in range(4):
    print(f"linha_{i}: {media_linhas[i]}", f"coluna_{i}: {media_colunas[i]}", sep=", ")

media_matriz = np.concatenate([media_linhas, media_colunas])
print("Maior Media entre as linhas e colunas: ", media_matriz.max())

values, counts = np.unique_counts(matriz_4x4)

counts_2 = {
    "values":[],
    "counts":[]
}
for i in range(len(values)):
    print(f"Numero: {values[i]}, Contage: {counts[i]}")
    if counts[i] == 2:
        counts_2["values"].append(int(values[i]))
        counts_2["counts"].append(int(counts[i]))

print("numeros que apareceram 2 vezes: ", counts_2["values"])        
        
