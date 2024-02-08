#Programa em que turno vc estuda


# Explicação do input
turno = input("Digite o turno que você estuda (M-matutino, V-vespertino, N-noturno): ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
