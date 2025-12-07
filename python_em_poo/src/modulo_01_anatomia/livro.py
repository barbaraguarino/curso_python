class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def descrever(self):
        return f"O livro {self.titulo} foi escrito por {self.autor} em {self.ano}"