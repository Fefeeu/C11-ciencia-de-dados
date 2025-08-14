# %%
def extremos_pessoas(pessoas:list):
    mais_leve = pessoas[0]
    mais_pesado = pessoas[0]
    
    for pessoa in pessoas:
        if mais_leve["peso"] > pessoa["peso"]:
            mais_leve = pessoa
        if mais_pesado["peso"] < pessoa["peso"]:
            mais_pesado = pessoa
    return mais_leve, mais_pesado
lista_pessoas = []

for i in range(3):
    pessoa = {}
    pessoa["nome"] = input(f"\nNome da pessoa {i}: ")
    pessoa["peso"] = float(input(f"Peso da pessoa {i}: "))
    lista_pessoas.append(pessoa)
    
mais_leve, mais_pesado = extremos_pessoas(lista_pessoas)

print(f"Pessoa mais leve: {mais_leve}")
print(f"Pessoa mais pesada: {mais_pesado}")

