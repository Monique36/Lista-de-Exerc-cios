#Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Não dividir por zero
if num2 != 0:
    divisao = num1 / num2
    print(f"Soma: {soma}, Subtração: {subtracao}, Multiplicação: {multiplicacao}, Divisão: {divisao}")
else:
    print("Não é possível dividir por zero.")
