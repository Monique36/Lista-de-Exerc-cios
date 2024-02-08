# Dicionário representando contatos


# Dicionário representando os contatos (nome: telefone)
contatos = {
    "João": "123456789",
    "Maria": "987654321",
    "Pedro": "456789123"
}

# Solicitar ao usuário o nome do contato a ser procurado
nome_contato = input("Digite o nome do contato que deseja procurar: ")

# Procurar o contato pelo nome e imprimir o telefone, se encontrado
if nome_contato in contatos:
    print(f"Telefone de {nome_contato}: {contatos[nome_contato]}")
else:
    print("Contato não encontrado.")
