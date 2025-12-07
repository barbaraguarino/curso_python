# from livro import Livro
from carro import Carro

def malhar_carro(carro, nova_cor):
    print(f"--- Entrando na oficina com o {carro.marca} ---")
    print(f"Cor atual: {carro.cor}")

    carro.cor = nova_cor
    print(f"O carro foi pintado de {nova_cor} dentro da função.")

    print("\n--- Saindo da oficina ---")

if __name__ == '__main__':

    """
    livro_1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro_2 = Livro("1984", "George Orwell", 1949)
    livro_3 = Livro("Dom Casmurro", "Machado de Assis", 1899)

    print("--- Meus Livros ---")
    print(livro_1.descrever())
    print(livro_2.descrever())
    print(livro_3.descrever())
    """

    """
    carro_1 = Carro("Toyota Corolla", "Prata")
    carro_2 = Carro("Honda Civic", "Preto")

    print("\n--- Detalhes dos Carros ---")
    print(carro_1.descricao())
    print(carro_2.descricao())

    print("\n--- Característica Compartilhada ---")
    print(f"O carro 1 tem {carro_1.quantidade_rodas} rodas.")
    print(f"O carro 2 tem {carro_2.quantidade_rodas} rodas.")

    print(f"O padrão da fábrica é: {Carro.quantidade_rodas} rodas.")
    """

    meu_fusca = Carro("Fusca", "Azul")
    print(f"1. Cor ORIGINAL do Fusca: {meu_fusca.cor}")

    malhar_carro(meu_fusca, "Amarelo")
    print(f"2. Cor do Fusca APÓS a função: {meu_fusca.cor}")