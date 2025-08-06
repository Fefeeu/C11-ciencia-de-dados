
sexo = input("Digite o sexo. M(masculino), F(feminino): ")


while(True):
    if sexo == "M":
        print("Voce é Masculino")
        break
    elif sexo == "F":
        print("Voce é Feminino")
        break
    else:
        sexo = input("Valor Invalido! Digite o sexo. M(masculino), F(feminino): ")
