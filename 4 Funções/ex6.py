#Jogo da forca
#Escolher aleatoriamente uma palavra secreta de uma lista predefinida.
#Inicializar uma string para representar a palavra secreta, substituindo cada letra por um espaço em branco.
#Permitir ao jogador ter um número limitado de tentativas (por exemplo, 6 tentativas).
#Em cada tentativa, solicitar ao jogador que forneça uma letra.
#Verificar se a letra fornecida pelo jogador está presente na palavra secreta.
#Se a letra estiver presente, revelá-la nas posições correspondentes na palavra secreta.
#Se a letra não estiver presente, informar uma mensagem de erro e reduzir o número de tentativas restantes.
#Continuar o jogo até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.


#biblioteca
import random

# Lista de palavras predefinidas
palavras = ["python", "programacao", "jogo", "computador", "algoritmo"]

def escolher_palavra():
    #Função para escolher aleatoriamente uma palavra da lista predefinida.
    return random.choice(palavras)

def inicializar_palavra_secreta(palavra):
    #Função para inicializar a palavra secreta com espaços em branco.
    return "_" * len(palavra)

def revelar_letra(palavra, palavra_secreta, letra):
    #Função para revelar a letra nas posições correspondentes na palavra secreta.
    nova_palavra_secreta = ""
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra_secreta += letra
        else:
            nova_palavra_secreta += palavra_secreta[i]
    return nova_palavra_secreta

# Escolher uma palavra secreta aleatoriamente
palavra_secreta = escolher_palavra()
# Inicializar a palavra secreta com espaços em branco
palavra_secreta_atual = inicializar_palavra_secreta(palavra_secreta)
# Número máximo de tentativas
max_tentativas = 6
# Lista para armazenar as letras já fornecidas pelo jogador
letras_fornecidas = []

print("Bem-vindo ao Jogo da Forca!")
print("Adivinhe a palavra secreta. Boa sorte!")

# Loop principal do jogo
while max_tentativas > 0:
    print("\nPalavra secreta:", palavra_secreta_atual)
    print("Tentativas restantes:", max_tentativas)
    letra = input("Digite uma letra: ").lower()

    # Verificar se a letra já foi fornecida anteriormente
    if letra in letras_fornecidas:
        print("Você já tentou esta letra. Tente outra.")
        continue

    # Adicionar a letra às letras fornecidas
    letras_fornecidas.append(letra)

    # Verificar se a letra está presente na palavra secreta
    if letra in palavra_secreta:
        print("Letra correta!")
        # Revelar a letra nas posições correspondentes na palavra secreta
        palavra_secreta_atual = revelar_letra(palavra_secreta, palavra_secreta_atual, letra)
    else:
        print("Letra incorreta.")
        # Reduzir o número de tentativas restantes
        max_tentativas -= 1

    # Verificar se o jogador acertou a palavra secreta
    if palavra_secreta_atual == palavra_secreta:
        print("\nParabéns! Você adivinhou a palavra secreta:", palavra_secreta)
        break

# Verificar se o jogador excedeu o número máximo de tentativas
if max_tentativas == 0:
    print("\nVocê excedeu o número máximo de tentativas. A palavra secreta era:", palavra_secreta)
