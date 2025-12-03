from livro import Livro

if __name__ == '__main__':
    livro_1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro_2 = Livro("1984", "George Orwell", 1949)
    livro_3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

    print("--- Meus Livros ---")
    print(f"Livro 1: {livro_1.titulo}, escrito por {livro_1.autor} em {livro_1.ano}")
    print(f"Livro 2: {livro_2.titulo}, escrito por {livro_2.autor} em {livro_2.ano}")
    print(f"Livro 3: {livro_3.titulo}, escrito por {livro_3.autor} em {livro_3.ano}")