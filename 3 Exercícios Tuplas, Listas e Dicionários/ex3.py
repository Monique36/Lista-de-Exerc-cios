#Crie um dicionário representando um carrinho de compras


# Dicionário representando o carrinho de compras (produto: quantidade)
carrinho = {
    "arroz": 2,
    "feijão": 3,
    "macarrão": 1,
    "carne": 2
}

# Dicionário representando o preço unitário de cada produto
precos_unitarios = {
    "arroz": 3.50,
    "feijão": 6.00,
    "macarrão": 2.00,
    "carne": 25.00
}

# Calculando o total do carrinho de compras
total = sum(precos_unitarios[produto] * quantidade for produto, quantidade in carrinho.items())

# Imprimindo o total do carrinho de compras
print("Total do carrinho de compras:", total)

