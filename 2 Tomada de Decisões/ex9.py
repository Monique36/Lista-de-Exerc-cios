#


pares = 0
impares = 0

# Solicitar os números ao usuário em uma linha separados por espaço
numeros = input("Digite os números separados por espaço (digite 0 para encerrar): ")

# Dividir os números fornecidos pelo usuário em uma lista
numeros = numeros.split()

# Iterar sobre cada número na lista
for numero_str in numeros:
    # Converter o número para inteiro
    numero = int(numero_str)

    # Verificar se o número é zero (encerramento do processo)
    if numero == 0:
        break
    # Verificar se o número é positivo
    elif numero < 0:
        print("Por favor, digite apenas números positivos.")
        continue

    # Contar números pares e ímpares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibir a quantidade de números pares e ímpares
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)

