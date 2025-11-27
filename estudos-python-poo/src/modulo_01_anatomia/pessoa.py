class Pessoa:
    # Uma classe simples representando uma Pessoa.

    def saudar(self):
        # Método que imprime uma saudação.
        # O parâmetro 'self' recebe a instância que está chamando este método.

        # Ao imprimir 'self', veremos o endereço de memória do objeto
        return f"Olá! Eu sou a instância: {self}"