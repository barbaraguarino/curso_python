from usuario import Usuario

if __name__ == '__main__':
    try:
        user = Usuario("test@gmail.com", "BoboDaCorte2026")

        print(user.descrever_usuario())

        user.senha = "NovaSenha10"
        print(user.descrever_usuario())

        user.senha = "123"

    except ValueError as e:
        print(f"ERRO CAPTURADO: {e}")