#Fazendo a conexão

import sqlite3

# Faz a conexão com o banco de dados
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Função para criar a tabela de alunos
def criar_tabela_alunos():
    consulta_criar_tabela = """
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            curso TEXT
        );
    """
    cursor.execute(consulta_criar_tabela)
    conexao.commit()

# Função para inserir registros na tabela de alunos
def inserir_alunos():
    dados_alunos = [
        ('João', 25, 'Engenharia'),
        ('Maria', 22, 'Medicina'),
        ('Monique', 39, 'Direito'),
        ('Ana', 23, 'Administração'),
        ('Lucas', 24, 'Engenharia')
    ]
    cursor.executemany("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", dados_alunos)
    conexao.commit()

# Função para executar as consultas básicas
def consultar_alunos():
    consulta_a = "SELECT * FROM alunos;"
    cursor.execute(consulta_a)
    print("\nConsulta a):")
    print(cursor.fetchall())

    consulta_b = "SELECT nome, idade FROM alunos WHERE idade > 20;"
    cursor.execute(consulta_b)
    print("\nConsulta b):")
    print(cursor.fetchall())

    consulta_c = "SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome;"
    cursor.execute(consulta_c)
    print("\nConsulta c):")
    print(cursor.fetchall())

    consulta_d = "SELECT COUNT(*) FROM alunos;"
    cursor.execute(consulta_d)
    print("\nConsulta d):")
    print(cursor.fetchone()[0])

# Função para atualizar a idade de um aluno específico
def atualizar_idade_aluno():
    consulta_atualizar = "UPDATE alunos SET idade = ? WHERE nome = ?;"
    cursor.execute(consulta_atualizar, (22, 'João'))
    conexao.commit()

# Função para remover um aluno pelo seu ID
def remover_aluno_por_id(id_aluno):
    consulta_remover = "DELETE FROM alunos WHERE id = ?;"
    cursor.execute(consulta_remover, (id_aluno,))
    conexao.commit()

# Função para criar a tabela de clientes e inserir registros
def criar_tabela_clientes():
    consulta_criar_tabela = """
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        saldo FLOAT
    );
    """
    cursor.execute(consulta_criar_tabela)
    dados_clientes = [
        ('Maria', 35, 1500.50),
        ('João', 40, 2000.75),
        ('Ana', 28, 800.25),
        ('Pedro', 45, 3000.00),
        ('Lucas', 50, 500.00)
    ]
    cursor.executemany("INSERT INTO clientes (nome, idade, saldo) VALUES (?, ?, ?)", dados_clientes)
    conexao.commit()

# Função para executar consultas e funções agregadas
def consultar_clientes():
    consulta_a = "SELECT nome, idade FROM clientes WHERE idade > 30;"
    cursor.execute(consulta_a)
    print("\nConsulta a):")
    print(cursor.fetchall())

    consulta_b = "SELECT AVG(saldo) FROM clientes;"
    cursor.execute(consulta_b)
    print("\nConsulta b):")
    print(cursor.fetchone()[0])

    consulta_c = "SELECT nome, MAX(saldo) FROM clientes;"
    cursor.execute(consulta_c)
    print("\nConsulta c):")
    print(cursor.fetchone())

    consulta_d = "SELECT COUNT(*) FROM clientes WHERE saldo > 1000;"
    cursor.execute(consulta_d)
    print("\nConsulta d):")
    print(cursor.fetchone()[0])

# Função para atualizar o saldo de um cliente específico
def atualizar_saldo_cliente():
    consulta_atualizar = "UPDATE clientes SET saldo = ? WHERE nome = ?;"
    cursor.execute(consulta_atualizar, (1600.00, 'Maria'))
    conexao.commit()

# Função para remover um cliente pelo seu ID
def remover_cliente_por_id(id_cliente):
    consulta_remover = "DELETE FROM clientes WHERE id = ?;"
    cursor.execute(consulta_remover, (id_cliente,))
    conexao.commit()

# Função para criar a tabela de compras e inserir registros
def criar_tabela_compras():
    consulta_criar_tabela = """
    CREATE TABLE IF NOT EXISTS compras (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto TEXT,
        valor REAL,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    );
    """
    cursor.execute(consulta_criar_tabela)
    dados_compras = [
        (1, 'Arroz', 20.50),
        (2, 'Feijão', 15.75),
        (3, 'Macarrão', 10.00),
        (4, 'Carne', 50.00),
        (5, 'Leite', 5.00)
    ]
    cursor.executemany("INSERT INTO compras (cliente_id, produto, valor) VALUES (?, ?, ?)", dados_compras)
    conexao.commit()

# Função para exibir as compras de cada cliente
def exibir_compras():
    consulta = """
    SELECT c.nome, co.produto, co.valor
    FROM clientes c
    JOIN compras co ON c.id = co.cliente_id;
    """
    cursor.execute(consulta)
    print("\nCompras de cada cliente:")
    for linha in cursor.fetchall():
        print(linha)

# Executa as funções
criar_tabela_alunos()
inserir_alunos()
consultar_alunos()
atualizar_idade_aluno()
remover_aluno_por_id(5)
criar_tabela_clientes()
consultar_clientes()
atualizar_saldo_cliente()
remover_cliente_por_id(3)
criar_tabela_compras()
exibir_compras()

# Fecha a conexão
conexao.close()

   



