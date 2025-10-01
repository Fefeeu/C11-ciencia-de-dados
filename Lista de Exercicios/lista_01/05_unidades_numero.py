numero = int(input("escrava um numero entre 1000 e 9999: "))

if 1000 <= numero <= 9999:
    numero = str(numero)
    
    print(f"Unidade: {numero[0]}")
    print(f"Dezena: {numero[1]}")
    print(f"Centena: {numero[2]}")
    print(f"Milhar: {numero[3]}")
    
    
else: 
    print("Numero Invalido")