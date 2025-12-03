class Carro:

    quantidade_rodas = 4

    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def descricao(self):
        return f"O carro é da marca {self.marca} na cor {self.cor}."