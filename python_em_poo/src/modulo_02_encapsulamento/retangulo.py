class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

if __name__ == "__main__":
    retangulo = Retangulo(5, 10)
    print(f"Área Inicial: {retangulo.area}") # Imprime 50

    # A MÁGICA:
    # Alteramos a largura. Não avisamos nada para a "area".
    retangulo.largura = 20

    # Ao acessar .area novamente, o cálculo roda de novo com o novo valor.
    print(f"Área Atualizada: {retangulo.area}") # Imprime 200 automaticamente!