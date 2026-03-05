class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.title()
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante)
    
    @property
    def ativo(self):
        return 'true' if self._ativo else 'false'



Restaurante('restaurante 1', 'Pizzaria')
Restaurante('restaurante 2', 'Marmitaria')

Restaurante.listar_restaurantes()