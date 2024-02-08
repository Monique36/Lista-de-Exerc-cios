#Função para contar vogais em uma string


def contar_vogais(frase):
    #Função que conta o número de vogais em uma frase.
    vogais = "aeiouAEIOU"
    total_vogais = sum(1 for letra in frase if letra in vogais)
    return total_vogais

frase = input("Digite uma frase: ")
total = contar_vogais(frase)
print("Total de vogais na frase:", total)
