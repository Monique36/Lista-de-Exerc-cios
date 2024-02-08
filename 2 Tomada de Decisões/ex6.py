#Verificando Login e senha

# Solicitar login e senha ao usuário
login = input("Digite o login: ")
senha = input("Digite a senha: ")

# Verificar se o login e a senha correspondem aos valores esperados
if login == "admin" and senha == "admin123":
    print("Acesso concedido!")
else:
    print("Login ou senha incorretos. Acesso negado!")
