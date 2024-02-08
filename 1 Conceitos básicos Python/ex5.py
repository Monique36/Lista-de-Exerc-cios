#Calculo do salário líquido
#Renda até R$ 1.903,98: isento de imposto de renda;
#Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
#Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
#Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
#Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

# Item 5
salario_bruto = float(input("Informe o salário bruto: "))
percentual_desconto = float(input("Informe o percentual de desconto do Imposto de Renda: "))

if salario_bruto <= 1903.98:
    salario_liquido = salario_bruto
elif 1903.99 <= salario_bruto <= 2826.65:
    salario_liquido = salario_bruto - (salario_bruto * (percentual_desconto / 100))
elif 2826.66 <= salario_bruto <= 3751.05:
    salario_liquido = salario_bruto - (salario_bruto * (percentual_desconto / 100))
elif 3751.06 <= salario_bruto <= 4664.68:
    salario_liquido = salario_bruto - (salario_bruto * (percentual_desconto / 100))
else:
    salario_liquido = salario_bruto - (salario_bruto * (percentual_desconto / 100))

print(f"O salário líquido é: R${salario_liquido:.2f}")
