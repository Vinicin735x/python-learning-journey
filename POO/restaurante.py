class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(restaurante)
    
restaurante_praca = Restaurante('Restaurante 1', 'Pizzaria')
restaurante_pizza = Restaurante('Restaurante 2', 'Marmitaria')

Restaurante.listar_restaurantes()