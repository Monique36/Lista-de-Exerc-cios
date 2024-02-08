#Calculo de Calorias


horas_exercicio_por_semana = float(input("Quantas horas de exercício físico você pratica por semana? "))

calorias_por_minuto = 5 # base de calculo
minutos_por_semana = horas_exercicio_por_semana * 60
calorias_por_semana = minutos_por_semana * calorias_por_minuto
calorias_por_mes = calorias_por_semana * 4  # Média de 4 semanas por mês

# Exibir o total de calorias queimadas em um mês
print("Total de calorias queimadas em um mês:", calorias_por_mes)
