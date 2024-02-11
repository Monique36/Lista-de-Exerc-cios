#Exercício Erros e Exceções

'''def calcular_media(valores):
    tamanho =1
    soma= 0.0
    for i, valor in enumerate(valores):
        soma+= valori += 1
media=soma/tamanho

continuar=True
valores=[]
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar=False

        media=calcular_media(valores)
        print('A média calculada para os valores {} foi de {}'.format(valores,media))'''

def calcular_media(valores):
    tamanho = len(valores)  # Obtém o tamanho da lista de valores
    soma = sum(valores)  # Calcula a soma dos valores na lista
    media = soma / tamanho if tamanho > 0 else 0  # Calcula a média, evitando divisão por zero
    return media  # Retorna a média calculada

continuar = True
valores = []  # Inicializa uma lista vazia para armazenar os valores digitados

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False  # Define continuar como False para sair do loop
    else:
        valor_numerico = float(valor)  # Converte a entrada para um número de ponto flutuante
        valores.append(valor_numerico)  # Adiciona o valor à lista de valores

media = calcular_media(valores)  # Chama a função calcular_media() para calcular a média dos valores
print('A média calculada para os valores {} foi de {}'.format(valores, media))  # Exibe a média calculada
