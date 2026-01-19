class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        if len(senha) < 8:
            raise ValueError("Senha inválida. Deve ter no mínimo 8 caracteres.")
        self.__senha = senha

    def descrever_usuario(self):
        return f"O usuário {self.email} possui uma senha salva: {self.__senha}."