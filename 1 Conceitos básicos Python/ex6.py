#Calculando o tempo de viagem de avião, carro e ônibus.
#Levando em consideração:
#avião = 600 km/h
#carro = 100 km/h
#ônibus = 80 km/h


def calcular_tempo_viagem(distancia, velocidade):
    # Função para calcular o tempo de viagem dado uma distância e uma velocidade
    tempo = distancia / velocidade
    return tempo

# Solicitar a distância da viagem ao usuário
distancia = float(input("Digite a distância da viagem em km: "))

# Calcular o tempo de viagem para avião, carro e ônibus
tempo_aviao = calcular_tempo_viagem(distancia, 600)
tempo_carro = calcular_tempo_viagem(distancia, 100)
tempo_onibus = calcular_tempo_viagem(distancia, 80)

# Exibir os resultados
print("Tempo de viagem de avião:", tempo_aviao, "horas")
print("Tempo de viagem de carro:", tempo_carro, "horas")
print("Tempo de viagem de ônibus:", tempo_onibus, "horas")
