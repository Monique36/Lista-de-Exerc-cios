#Permite que o usuário digite se nome e em seguida mostre o nome de trás para a frente


# Solicitar ao usuário o nome
nome = input("Digite seu nome: ")

# Reverter o nome e transformar em letras maiúsculas
nome_invertido = nome[::-1].upper()

# Imprimir o nome invertido em letras maiúsculas
print("Nome invertido em letras maiúsculas:", nome_invertido)
