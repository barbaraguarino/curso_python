from pessoa import Pessoa

if __name__ == '__main__':
    # Instanciando dois objetos diferentes (ocupam lugares diferentes na memória)
    pessoa_a = Pessoa()
    pessoa_b = Pessoa()

    # Chamada do método: O Python passa 'pessoa_a' para o 'self' automaticamente
    print(pessoa_a.saudar())

    # Chamada do método: O Python passa 'pessoa_b' para o 'self' automaticamente
    print(pessoa_b.saudar())

    # PROVA REAL:
    # O que acontece se tentarmos chamar o método pela Classe passando o objeto manualmente?
    # Isso é exatamente o que o Python faz por trás dos panos:
    print("\n--- Chamada Manual (O que o Python faz internamente) ---")
    print(Pessoa.saudar(pessoa_a))