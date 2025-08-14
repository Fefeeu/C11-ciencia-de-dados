# %%
aluno = {}

nome_aluno = input("Nome Aluno: ")
media_aluno = int(input("Média Aluno: "))

aluno["nome"] = nome_aluno
aluno["media"] = media_aluno

if aluno["media"] >= 50:
    aluno["status"] = "AP"
else: 
    aluno["media"] = "RP"

print("\nO aluno esta: ", aluno["status"])

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")