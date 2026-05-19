from restaurante import Restaurante
from cardapio.item_cardapio import Bebida
from cardapio.item_cardapio import Prato


restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato = Prato('Pão de sal', 2.00, 'O pão mais quente da cidade')

def main():
    print(bebida_suco)
    print(prato)

if __name__ == '__main__':
    main()