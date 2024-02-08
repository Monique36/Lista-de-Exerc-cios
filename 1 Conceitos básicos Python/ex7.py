#Calcule o Índice de Massa Corporal(IMC)


peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcular o IMC usando a fórmula: IMC = peso / (altura x altura)
imc = peso / (altura * altura)

# Exibir o IMC calculado
print("O Índice de Massa Corporal (IMC) é:", imc)
