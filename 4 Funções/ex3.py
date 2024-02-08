#Funções de conversão de temperatura e menu


def celsius_para_fahrenheit(celsius):
    #Função que converte temperatura de Celsius para Fahrenheit.
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    #Função que converte temperatura de Fahrenheit para Celsius.
    return (fahrenheit - 32) * 5/9

def menu_conversao():
    #Função que exibe o menu de opções de conversão.
    print("Escolha a opção de conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    opcao = int(input("Opção: "))
    return opcao

opcao = menu_conversao()

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print("A temperatura em Fahrenheit é:", resultado)
elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print("A temperatura em Celsius é:", resultado)
else:
    print("Opção inválida")

