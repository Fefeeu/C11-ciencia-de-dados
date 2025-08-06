distancia = float(input("Distancia em Km: "))

if 0 <= distancia <= 200:
    print("A passagem ira custar: ", distancia*0.5)
elif distancia > 200:
    print("A passagem ira custar: ", distancia*0.45)
else:
    print("Valor da distancia invalido") 