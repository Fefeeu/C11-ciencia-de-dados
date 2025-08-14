# %%
n = int(input("Numero de pessoas: "))

lista_pessoas = []

for i in range(n):
    pessoa = {}
    pessoa["nome"] = input(f"Nome da pessoa {i}: ")
    pessoa["idade"] = int(input(f"Idade da pessoa {i}: "))
    pessoa["sexo"] = input(f"Sexo da pessoa {i}: ")
    lista_pessoas.append(pessoa)

media = 0
contador = 0
for pessoa in lista_pessoas:
    media += pessoa["idade"]
    if pessoa["sexo"] == "F" and pessoa["idade"] < 20:
        contador += 1

media = media/len(lista_pessoas)

print(f"Media de idade: {media}\n")
print(f"Mulheres com menos de 20 anos: {contador}")
