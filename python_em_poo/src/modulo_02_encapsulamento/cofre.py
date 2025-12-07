class Cofre:
    def __init__(self, segredo, tesouro):
        self._segredo = segredo
        self.__tesouro = tesouro

    def mostrar_tesouro_de_forma_segura(self):
        print(f"Acesso autorizado. O tesouro é: {self.__tesouro}")


if __name__ == "__main__":
    meu_cofre = Cofre("Senhanova", "Diamantes")

    print("--- Tentando acessar o atributo Protected (_) ---")
    print(f"Segredo: {meu_cofre._segredo}")

    print("\n--- Tentando acessar o atributo Private (__) ---")
    try:
        print(f"Tesouro: {meu_cofre.__tesouro}")
    except AttributeError as e:
        print(f"ERRO BLOQUEADO: {e}")

    print("\n--- Acessando da forma correta ---")
    meu_cofre.mostrar_tesouro_de_forma_segura()

    print(f"\nHackeando o cofre: {meu_cofre._Cofre__tesouro}")