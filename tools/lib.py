import json

class Book():
    """Classe de registro de livros"""
    
    def __init__(self, titulo: str, autor: str, genero: str, estoque: int) -> None:
        """Instâncias do livro"""
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estoque = estoque
    

    def acervo(self=None) -> dict:
        with open("data/books.json", "r", encoding="utf-8") as file:
            conteudo = file.read()
    
        return json.loads(conteudo)
    
    def registrar(self) -> None:
        """Função para registrar o livro"""
        dados = self.acervo()
        dados[self.titulo] = {
            "Autor": self.autor,
            "Genero": self.genero,
            "Estoque": self.estoque
        }

        with open("data/books.json", "w", encoding="utf-8") as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)

    def view(self):
        """Vizualização de dados"""
        return {"titulo": self.titulo, "autor": self.autor, "genero": self.genero, "estoque": self.estoque}

    def requirements():
        """Dados requeridos para registrar um livro"""
        return [[str, "titulo"], [str, "autor"], [str, "genero"], [int, "estoque"]]


class User():
    def __init__(self, nome: str, cpf: str, idade: int) -> None:
        """Informações do usuário"""
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
    
    def usuarios(self=None) -> dict:
        with open("data/users.json", "r", encoding="utf-8") as file:
            conteudo = file.read()

        return json.loads(conteudo)
    
    def requirements():
        """Dados requeridos para registrar um livro"""
        return [[str, "Nome"], [str, "CPF"], [int, "Idade"]]
    
    def view(self):
        """Vizualização de dados"""
        return {"Nome": self.nome, "CPF": self.cpf, "idade": self.idade}
    
    def registrar(self) -> None:
        """Função para registrar o livro"""
        dados = self.usuarios()
        dados[self.cpf] = {
            "Nome": self.nome,
            "Idade": self.idade,
            "Histórico": []
        }

        with open("data/users.json", "w", encoding="utf-8") as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)