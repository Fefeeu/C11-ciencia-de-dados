lista = ["Goku", "Vegeta", "Trunks", "Gohan"]
print(lista, end="\n\n")

lista.append("Buma")

print(lista, end="\n\n")

lista.insert(2, "teste") 
print(lista, end="\n\n")

del lista[0]
print(lista, end="\n\n")

lista.remove("Trunks")
print(lista, end="\n\n")


lista.sort()