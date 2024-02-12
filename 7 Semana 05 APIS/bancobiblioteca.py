import sqlite3

# Conectando ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('biblioteca.db')

# Criando um cursor para executar comandos SQL
cursor = conn.cursor()

# Criando tabelas
cursor.execute('''CREATE TABLE IF NOT EXISTS Autores (
                    autor_id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Editoras (
                    editora_id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Livros (
                    livro_id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    editora_id INTEGER,
                    FOREIGN KEY (editora_id) REFERENCES Editoras(editora_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Exemplares (
                    exemplar_id INTEGER PRIMARY KEY,
                    livro_id INTEGER,
                    disponivel BOOLEAN DEFAULT TRUE,
                    FOREIGN KEY (livro_id) REFERENCES Livros(livro_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                    usuario_id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    nacionalidade TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Emprestimos (
                    emprestimo_id INTEGER PRIMARY KEY,
                    exemplar_id INTEGER,
                    usuario_id INTEGER,
                    data_emprestimo DATE,
                    data_devolucao DATE,
                    devolvido BOOLEAN DEFAULT FALSE,
                    FOREIGN KEY (exemplar_id) REFERENCES Exemplares(exemplar_id),
                    FOREIGN KEY (usuario_id) REFERENCES Usuarios(usuario_id)
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS AutoresLivros (
                    autor_id INTEGER,
                    livro_id INTEGER,
                    FOREIGN KEY (autor_id) REFERENCES Autores(autor_id),
                    FOREIGN KEY (livro_id) REFERENCES Livros(livro_id)
                )''')

# Inserindo dados de exemplo
cursor.executemany('''INSERT INTO Autores (nome) VALUES (?)''', [('Stephen King',), ('J.K. Rowling',), ('George Orwell',)])
cursor.executemany('''INSERT INTO Editoras (nome) VALUES (?)''', [('Editora A',), ('Editora B',), ('Editora C',)])
cursor.executemany('''INSERT INTO Livros (titulo, editora_id) VALUES (?, ?)''', [('It', 1), ('Harry Potter', 2), ('1984', 3)])
cursor.executemany('''INSERT INTO Exemplares (livro_id) VALUES (?)''', [(1,), (2,), (3,), (3,), (3,)])
cursor.executemany('''INSERT INTO Usuarios (nome, telefone, nacionalidade) VALUES (?, ?, ?)''', [('João', '123456789', 'Brasil'), ('Maria', '987654321', 'Brasil')])
cursor.executemany('''INSERT INTO Emprestimos (exemplar_id, usuario_id, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)''', [(1, 1, '2024-01-01', '2024-02-01'), (2, 2, '2024-01-05', '2024-02-05')])

# Salvando as alterações
conn.commit()

# Consultas SQL
# Listar todos os livros disponíveis
cursor.execute('''SELECT Livros.titulo, COUNT(Exemplares.exemplar_id) AS copias_disponiveis
                    FROM Livros
                    LEFT JOIN Exemplares ON Livros.livro_id = Exemplares.livro_id
                    WHERE Exemplares.disponivel = 1
                    GROUP BY Livros.titulo''')
print("Livros disponíveis:")
for row in cursor.fetchall():
    print(row)

# Encontrar todos os livros emprestados no momento
cursor.execute('''SELECT Livros.titulo
                    FROM Livros
                    INNER JOIN Exemplares ON Livros.livro_id = Exemplares.livro_id
                    INNER JOIN Emprestimos ON Exemplares.exemplar_id = Emprestimos.exemplar_id
                    WHERE Emprestimos.devolvido = 0''')
print("\nLivros emprestados no momento:")
for row in cursor.fetchall():
    print(row)

# Localizar os livros escritos por um autor específico
cursor.execute('''SELECT Livros.titulo
                    FROM Livros
                    INNER JOIN AutoresLivros ON Livros.livro_id = AutoresLivros.livro_id
                    INNER JOIN Autores ON AutoresLivros.autor_id = Autores.autor_id
                    WHERE Autores.nome = ?''', ('Stephen King',))
print("\nLivros escritos por Stephen King:")
for row in cursor.fetchall():
    print(row)

# Verificar o número de cópias disponíveis de um determinado livro
cursor.execute('''SELECT Livros.titulo, COUNT(Exemplares.exemplar_id) AS copias_disponiveis
                    FROM Livros
                    LEFT JOIN Exemplares ON Livros.livro_id = Exemplares.livro_id
                    WHERE Livros.titulo = ? AND Exemplares.disponivel = 1''', ('It',))
print("\nNúmero de cópias disponíveis de 'It':")
for row in cursor.fetchall():
    print(row)

# Mostrar os empréstimos em atraso
cursor.execute('''SELECT Usuarios.nome AS usuario, Livros.titulo AS livro, Emprestimos.data_devolucao
                    FROM Emprestimos
                    INNER JOIN Usuarios ON Emprestimos.usuario_id = Usuarios.usuario_id
                    INNER JOIN Exemplares ON Emprestimos.exemplar_id = Exemplares.exemplar_id
                    INNER JOIN Livros ON Exemplares.livro_id = Livros.livro_id
                    WHERE Emprestimos.data_devolucao < DATE('now') AND Emprestimos.devolvido = 0''')
print("\nEmpréstimos em atraso:")
for row in cursor.fetchall():
    print(row)

# Funções adicionadas
def marcar_livro_devolvido(livro_id):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Atualiza o status do livro para devolvido
    cursor.execute('''UPDATE Emprestimos 
                      SET devolvido = TRUE 
                      WHERE exemplar_id = ?''', (livro_id,))

    conn.commit()
    conn.close()

def remover_autor(nome_autor):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Exclui o autor e todas as suas associações com livros
    cursor.execute('''DELETE FROM Autores 
                      WHERE nome = ?''', (nome_autor,))

    conn.commit()
    conn.close()

# Função para consultar e gerenciar o sistema
def main():
    # Exemplos de utilização das novas funções
    marcar_livro_devolvido(1)
    remover_autor('Stephen King')

if __name__ == "__main__":
    main()

# Fechando a conexão
conn.close()





