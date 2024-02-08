#Programa para converter dinheiro para moedas estrangeiras


def converter_para_moeda(valor, taxa):
    #Função que converte um valor em uma moeda para outra, usando uma taxa de conversão.
    return valor / taxa

carteira = float(input("Quanto dinheiro você tem na carteira? "))

#tabela base

tabela_conversion = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suiço": 0.42,
    "Euro": 5.36,
    "Libra esterlina": 6.21
}

for moeda, taxa in tabela_conversion.items():
    quantidade_moeda = converter_para_moeda(carteira, taxa)
    print(f"Com R$ {carteira:.2f}, você pode comprar {quantidade_moeda:.2f} {moeda}")
