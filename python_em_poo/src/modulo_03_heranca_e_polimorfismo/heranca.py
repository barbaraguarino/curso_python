class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def descricao_gerente(self):
        return f"{self.nome}: Salário Base de {self.salario} + Bônus de {self.bonus}%."

if __name__ == '__main__':
    gerente = Gerente('Fernando Monteiro', 2000, 50)
    print(gerente.descricao_gerente())