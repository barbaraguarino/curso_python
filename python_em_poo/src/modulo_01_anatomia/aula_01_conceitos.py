class Caneta:

    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

    def descrever(self):
        return f"Caneta da marca {self.marca} da cor {self.cor}."

if __name__ == '__main__':
    caneta_1 = Caneta("azul", "Bic")
    caneta_2 = Caneta("vermelha", "Faber")

    print(caneta_1.descrever())
    print(caneta_2.descrever())