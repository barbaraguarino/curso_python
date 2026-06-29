# Declaração de Classe

class Gafanhoto:

    #Método Construtor
    def __init__(self):
        # Atributos de Instância
        self.nome = ''
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos

#Instanciamento da classe, ou seja, criação do objeto.
g1 = Gafanhoto()

g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 35
print(g2.mensagem())