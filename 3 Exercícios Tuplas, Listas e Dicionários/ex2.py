# Calcule a média dos alunos e imprima os alunos com média maior ou igual a 7

# Lista para armazenar as médias dos alunos
medias = []

# Loop para pedir as notas dos alunos e calcular suas médias
for i in range(5):
    notas = [float(input(f"Digite a nota {j + 1} do aluno {i + 1}: ")) for j in range(4)]
    media = sum(notas) / len(notas)
    medias.append(media)

# Contagem de alunos com média maior ou igual a 7.0
alunos_aprovados = sum(1 for media in medias if media >= 7.0)

# Imprimir o número de alunos aprovados
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
