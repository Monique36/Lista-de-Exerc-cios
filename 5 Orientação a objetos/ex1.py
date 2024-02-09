#Exercícios Classes e Objetos
#1. Crie uma classe que modele o objeto "carro".
#2. Um carro tem os seguintes atributos: ligado, cor, modelo,velocidade.
#3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,desacelera.
#4. Crie uma instância da classe carro.
#5. Faça o carro "andar" utilizando os métodos da sua classe.
#6. Faça o carro "parar" utilizando os métodos da sua classe.


class Carro:
    def __init__(self, cor, modelo):
        # Método construtor que inicializa os atributos do carro
        self.cor = cor  # Atributo para armazenar a cor do carro
        self.modelo = modelo  # Atributo para armazenar o modelo do carro
        self.ligado = False  # Atributo para armazenar se o carro está ligado ou não
        self.velocidade = 0  # Atributo para armazenar a velocidade atual do carro

    def liga(self):
        # Método para ligar o carro
        if not self.ligado:  # Verifica se o carro já está ligado
            self.ligado = True  # Define o carro como ligado
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        # Método para desligar o carro
        if self.ligado:  # Verifica se o carro está ligado
            self.ligado = False  # Define o carro como desligado
            self.velocidade = 0  # Zera a velocidade do carro ao desligar
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelera(self, velocidade):
        # Método para acelerar o carro
        if self.ligado:  # Verifica se o carro está ligado
            self.velocidade += velocidade  # Incrementa a velocidade do carro
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("Não é possível acelerar, o carro está desligado.")

    def desacelera(self, velocidade):
        # Método para desacelerar o carro
        if self.ligado:  # Verifica se o carro está ligado
            self.velocidade -= velocidade  # Decrementa a velocidade do carro
            if self.velocidade < 0:
                self.velocidade = 0  # Garante que a velocidade não seja negativa
            print(f"O carro desacelerou para {self.velocidade} km/h.")
        else:
            print("Não é possível desacelerar, o carro está desligado.")

# Solicita ao usuário a inserção da cor e modelo do carro
cor_carro = input("Digite a cor do carro: ")
modelo_carro = input("Digite o modelo do carro: ")

# Criando uma instância da classe Carro com os dados inseridos pelo usuário
meu_carro = Carro(cor=cor_carro, modelo=modelo_carro)

# Exibe a cor e modelo do carro criado
print(f"\nCor do carro: {meu_carro.cor}")
print(f"Modelo do carro: {meu_carro.modelo}\n")

# Ligar o carro
meu_carro.liga()

# Acelerar o carro
meu_carro.acelera(50)

# Desacelerar o carro
meu_carro.desacelera(20)

# Parar o carro
meu_carro.desliga()


