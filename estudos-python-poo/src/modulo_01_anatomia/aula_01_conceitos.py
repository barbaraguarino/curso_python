# Definição da Classe (O Molde)
class Caneta:
    # O Inicializador
    # self: refere-se ao objeto que acabou de ser criado (falaremos mais dele depois)
    # cor, marca: são os argumentos que passamos ao criar a caneta
    def __init__(self, cor, marca):
        # Aqui estamos anexando dados ao objeto
        self.cor = cor
        self.marca = marca
        print(f"Uma nova caneta {marca} {cor} foi criada!")

# Instanciação (Fabricando Objetos)
# Note que passamos 'Azul' e 'Bic', mas não passamos o self.
# O Python passa o objeto recém-criado como 'self' automaticamente.
caneta_1 = Caneta("Azul", "Bic")
caneta_2 = Caneta("Vermelha", "Faber")

# Acessando os atributos que definimos no __init__
print(f"Objeto 1: {caneta_1.marca} - {caneta_1.cor}")
print(f"Objeto 2: {caneta_2.marca} - {caneta_2.cor}")