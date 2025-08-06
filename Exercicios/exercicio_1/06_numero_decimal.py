from math import sqrt

numero = float(input("Entre com um numero com casas decimais: "))

print("Raiz: ", sqrt(numero))
print("Teto: ", numero.__ceil__())
print("Chão: ", numero.__floor__())
print("Parte Inteira: ", numero.__trunc__())

