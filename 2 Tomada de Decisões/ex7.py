#Programa que identifique se é idoso, adulto, adolescente ou criança


# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Identificar faixa etária com base na idade fornecida
if idade < 13:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 65:
    print("Adulto")
else:
    print("Idoso")
