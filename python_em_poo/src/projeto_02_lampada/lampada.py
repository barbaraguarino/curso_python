class Lampada:

    def __init__(self):
        self.estado = False
        self.luminosidade = 0

    def ligar(self):
        self.estado = True
        if self.luminosidade == 0:
            self.luminosidade = 100

    def desligar(self):
        self.estado = False
        if self.luminosidade == 100:
            self.luminosidade = 0

    def ajustar_luminosidade(self, valor):
        if valor > 100:
            self.luminosidade = 100
        elif valor < 0:
            self.luminosidade = 0
        else:
            self.luminosidade = valor

    def mostrar_estado(self):
        if self.estado:
            return f"A lâmpada está LIGADA com {self.luminosidade}% de brilho."
        else:
            return f"A lâmpada está DESLIGADA."