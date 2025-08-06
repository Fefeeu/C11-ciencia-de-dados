def count_characteres(nome:str) -> int:
    return nome.count("") - nome.count(" ") - 1
    

nome = input()

print(nome.upper())
print(nome.lower())
print(count_characteres(nome))

nomes = nome.split(" ")
nomes[-1] = "do Inatel"

nome = " ".join(nomes)

print(nome)
