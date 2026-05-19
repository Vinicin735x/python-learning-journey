class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome 
        self._preco = preco

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.decricao = descricao

    def __str__(self):
        return self._nome

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def __str__(self):
        return self._nome