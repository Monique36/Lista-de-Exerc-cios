# Determinando o maior entre 3 números


# Solicitar três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Determinar o maior número utilizando estruturas condicionais
if num1 >= num2 and num1 >= num3:
    print("O maior número é:", num1)
elif num2 >= num1 and num2 >= num3:
    print("O maior número é:", num2)
else:
    print("O maior número é:", num3)
