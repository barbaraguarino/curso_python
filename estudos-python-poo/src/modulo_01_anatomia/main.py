from livro import Livro

if __name__ == '__main__':
    livro_1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro_2 = Livro("1984", "George Orwell", 1949)
    livro_3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

    print("--- Meus Livros ---")
    print(livro_1.descrever())
    print(livro_2.descrever())
    print(livro_3.descrever())