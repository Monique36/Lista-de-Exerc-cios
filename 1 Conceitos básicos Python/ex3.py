#Programa para converter quilômetros em metros, centímetros e milímetros


quilometros = float(input("Informe a quantidade de quilômetros: "))
metros = quilometros * 1000
centimetros = quilometros * 100000
milimetros = quilometros * 1000000

print(f"{quilometros} quilômetros equivalem a {metros} metros, {centimetros} centímetros e {milimetros} milímetros.")
