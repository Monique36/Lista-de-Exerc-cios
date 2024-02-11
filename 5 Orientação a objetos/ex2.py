#O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
#Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
#● Cada conta corrente pode ter um ou mais clientes como titular.
#● O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
#● A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#● Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
#● Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até renda_mensal.
#● Clientes homens por enquanto não têm direito a cheque especial.
#Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata



from abc import ABC, abstractmethod  # Importa o módulo ABC para trabalhar com classes abstratas

class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal  # Atributos de nome, telefone e renda mensal do cliente

class ContaCorrente(ABC):  # Define uma classe abstrata para representar uma conta corrente
    def __init__(self, clientes):
        self.clientes = clientes  # Lista de clientes titulares da conta
        self.saldo = 0  # Saldo inicial da conta
        self.operacoes = []  # Lista de operações realizadas na conta

    def sacar(self, valor):  # Método para sacar dinheiro da conta
        if self.saldo - valor >= 0:  # Verifica se há saldo suficiente na conta
            self.saldo -= valor  # Atualiza o saldo após o saque
            self.operacoes.append(f"Saque de R${valor}")  # Registra a operação na lista de operações
            return True  # Retorna True indicando que o saque foi realizado com sucesso
        else:
            return False  # Retorna False indicando que o saque não pôde ser realizado devido ao saldo insuficiente

    def depositar(self, valor):  # Método para depositar dinheiro na conta
        self.saldo += valor  # Atualiza o saldo após o depósito
        self.operacoes.append(f"Depósito de R${valor}")  # Registra a operação na lista de operações

    @abstractmethod  # Define um método abstrato
    def cheque_especial(self):  # Método abstrato para calcular o cheque especial
        pass

class ContaCorrenteMulher(ContaCorrente):  # Define uma subclasse de ContaCorrente para clientes mulheres
    def cheque_especial(self):  # Implementa o método para calcular o cheque especial
        return self.clientes[0].renda_mensal  # Retorna o valor do cheque especial, igual à renda mensal da primeira cliente

class ContaCorrenteHomem(ContaCorrente):  # Define uma subclasse de ContaCorrente para clientes homens
    def cheque_especial(self):  # Implementa o método para calcular o cheque especial
        return 0  # Retorna zero, pois homens não têm direito a cheque especial

# Exemplo de uso das classes
cliente1 = Cliente("Maria", "123456789", 5000)  # Cria um cliente Maria com telefone e renda mensal
conta_maria = ContaCorrenteMulher([cliente1])  # Cria uma conta corrente para Maria (mulher)

cliente2 = Cliente("João", "987654321", 4000)  # Cria um cliente João com telefone e renda mensal
conta_joao = ContaCorrenteHomem([cliente2])  # Cria uma conta corrente para João (homem)

conta_maria.depositar(2000)  # Maria deposita R$ 2000 na sua conta
print(f"Saldo da conta de Maria: R${conta_maria.saldo}")  # Exibe o saldo da conta de Maria

conta_maria.sacar(7000)  # Maria tenta sacar R$ 7000, valor superior ao cheque especial
print(f"Saldo da conta de Maria após saque: R${conta_maria.saldo}")  # Exibe o saldo da conta de Maria após tentativa de saque

conta_joao.depositar(1000)  # João deposita R$ 1000 na sua conta
print(f"Saldo da conta de João: R${conta_joao.saldo}")  # Exibe o saldo da conta de João

