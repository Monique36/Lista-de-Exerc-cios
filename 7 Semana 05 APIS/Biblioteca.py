from abc import ABC, abstractmethod # importando biblioteca

#declarando as classes
class Pessoa:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

class Autor(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)

class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)

class Livro:
    def __init__(self, titulo, editora, generos, exemplares_disponiveis, max_renovacoes=None):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares_disponiveis = exemplares_disponiveis
        self.max_renovacoes = max_renovacoes

class Exemplar:
    def __init__(self, livro):
        self.livro = livro
        self._emprestado = False  # Atributo privado que armazena o estado de empréstimo

    @property
    def emprestado(self):  # Getter para o atributo _emprestado
        return self._emprestado

    @emprestado.setter
    def emprestado(self, value):  # Setter para o atributo _emprestado
        self._emprestado = value

class Emprestimo:
    def __init__(self, exemplar, usuario, data_emprestimo, data_devolucao, estado):
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado = estado # Pode ser "emprestado" ou "devolvido"

class Biblioteca:
    def __init__(self):
        self.usuarios = []  # Lista para armazenar os usuários da biblioteca
        self.livros = []  # Lista para armazenar os livros disponíveis na biblioteca
        self.emprestimos = []  # Lista para armazenar os empréstimos realizados

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)  # Adiciona um novo usuário à lista de usuários

    def adicionar_livro(self, livro):
        self.livros.append(livro)  # Adiciona um novo livro à lista de livros

    def emprestar_exemplar(self, exemplar, usuario, data_emprestimo, data_devolucao):
        if exemplar.emprestado:
            print("Este exemplar já está emprestado.")
        else:
            exemplar.emprestado = True  # Marca o exemplar como emprestado
            emprestimo = Emprestimo(exemplar, usuario, data_emprestimo, data_devolucao, "emprestado")
            self.emprestimos.append(emprestimo)  # Registra o empréstimo na lista de empréstimos

    def devolver_exemplar(self, exemplar):
        exemplar.emprestado = False  # Marca o exemplar como não emprestado
        for emprestimo in self.emprestimos:
            if emprestimo.exemplar == exemplar:
                emprestimo.estado = "devolvido"  # Atualiza o estado do empréstimo para devolvido
                break  # Sai do loop após encontrar o empréstimo correspondente

# Classe abstrata para definir métodos comuns para diferentes tipos de pessoas
class Pessoa(ABC):
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    @abstractmethod
    def informacao_pessoa(self):
        pass

class Autor(Pessoa):
    def __init__(self, nome, telefone, nacionalidade, obras_publicadas):
        super().__init__(nome, telefone, nacionalidade)
        self.obras_publicadas = obras_publicadas

    def informacao_pessoa(self):  # Método implementado para a classe abstrata Pessoa
        print(f"Autor: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}, Obras Publicadas: {self.obras_publicadas}")

class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade, data_inscricao):
        super().__init__(nome, telefone, nacionalidade)
        self.data_inscricao = data_inscricao

    def informacao_pessoa(self):  # Método implementado para a classe abstrata Pessoa
        print(f"Usuário: {self.nome}, Telefone: {self.telefone}, Nacionalidade: {self.nacionalidade}, Data de Inscrição: {self.data_inscricao}")


if __name__ == "__main__":
    # Criando uma biblioteca
    biblioteca = Biblioteca()

    # Adicionando usuários
    usuario1 = Usuario("João", "123456789", "Brasil", "01/01/2024")
    usuario2 = Usuario("Maria", "987654321", "Brasil", "01/01/2024")
    biblioteca.adicionar_usuario(usuario1)
    biblioteca.adicionar_usuario(usuario2)

    # Adicionando livros
    livro1 = Livro("Python for Beginners", "Editora A", ["Programação", "Python"], 5, 2)
    livro2 = Livro("Data Science Handbook", "Editora B", ["Data Science", "Python"], 3)
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)

    # Realizando empréstimos
    biblioteca.emprestar_exemplar(Exemplar(livro1), usuario1, "01/02/2024", "01/03/2024")
    biblioteca.emprestar_exemplar(Exemplar(livro2), usuario2, "01/02/2024", "01/03/2024")

    # Devolvendo exemplares
    biblioteca.devolver_exemplar(Exemplar(livro1))

    # Exibindo informações dos usuários
    for usuario in biblioteca.usuarios:
        usuario.informacao_pessoa()

    # Exibindo informações dos livros
    for livro in biblioteca.livros:
        print(f"Título: {livro.titulo}, Editora: {livro.editora}, Gêneros: {livro.generos}, Exemplares Disponíveis: {livro.exemplares_disponiveis}")

    # Exibindo informações dos empréstimos
    for emprestimo in biblioteca.emprestimos:
        print(f"Exemplar: {emprestimo.exemplar.livro.titulo}, Usuário: {emprestimo.usuario.nome}, Data de Empréstimo: {emprestimo.data_emprestimo}, Data de Devolução: {emprestimo.data_devolucao}")
