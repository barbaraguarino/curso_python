class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_info(self):
        return f"Matrícula: {self.matricula} - Nome: {self.nome}"