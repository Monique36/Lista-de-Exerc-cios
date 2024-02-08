#Mostrando 3 números em ordem crescente


# Solicitar três números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Criar uma lista com os números e ordená-la
lista_numeros = [num1, num2, num3]
lista_numeros.sort()

# Exibir os números em ordem crescente
print("Números em ordem crescente:", lista_numeros)
