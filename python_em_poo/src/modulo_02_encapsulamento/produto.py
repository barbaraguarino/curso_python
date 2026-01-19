class Produto:
    def __init__(self, preco):
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        if preco < 0:
            raise ValueError("O preço não pode ser negativo!")
        self._preco = preco

if __name__ == '__main__':
    produto = Produto(30)
    print(produto.preco)
    produto.preco = 20
    print(produto.preco)