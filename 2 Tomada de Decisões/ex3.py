#Faça um programa que peça uma nota, entre zero e dez.


# Estrutura de repetição
while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if 0 <= nota <= 10:
        break
    else:
        print("Valor inválido. Tente novamente.")

print(f"Você inseriu a nota: {nota}")

