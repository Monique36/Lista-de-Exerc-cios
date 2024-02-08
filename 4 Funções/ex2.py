# Função para retornar o reverso de um número inteiro


def reverso_numero(numero):
    return int(str(numero)[::-1])

# uso da função
numero = 127
reverso = reverso_numero(numero)
print("O reverso de", numero, "é:", reverso)

