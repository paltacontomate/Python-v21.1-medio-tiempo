from card import Card
import random

class Deck:

    def __init__(self):
        
        palos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.cards = []

        for s in palos:
            for i in valores:
                str_val = ""
                if i == 'As':
                    str_val = "Ace"
                elif i == 'J':
                    str_val = "Jack"
                elif i == 'Q':
                    str_val = "Queen"
                elif i == 'K':
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
                    card.card_info()

#Juego de Giro Y retiro

baraja = {'As': 11, 'Dos': 2, 'Tres': 3, 'Cuatro': 4, 'Cinco': 5, 'Seis': 6,
        'Siete': 7, 'Ocho': 8, 'Nueve': 9, 'Diez': 10, 'Jota': 10, 'Reina': 10, 'Rey': 10}

# Definir la función para repartir una carta aleatoria
def repartir_carta():
    carta = random.choice(list(baraja.keys()))
    return (carta, baraja[carta])

# Definir la función para sumar los valores de una mano
def sumar_mano(mano):
    suma = sum([carta[1] for carta in mano])
    for carta in mano:
        if carta[0] == 'As' and suma > 21:
            suma -= 10
    return suma

# Definir la función para jugar una mano
def jugar_mano():
    mano = []
    mano.append(repartir_carta())
    mano.append(repartir_carta())
    
    while True:
        print('Tu mano:', [carta[0] for carta in mano])
        print('Suma de tu mano:', sumar_mano(mano))
        if sumar_mano(mano) > 21:
            print('Te has pasado de 21. Pierdes.')
            return -1
        elif sumar_mano(mano) == 21:
            print('Has conseguido 21. Ganaste.')
            return 1
        else:
            respuesta = input('¿Quieres otra carta? (s/n): ')
            if respuesta == 's':
                mano.append(repartir_carta())
            else:
                break
    print('Tu mano final:', [carta[0] for carta in mano])
    print('Suma de tu mano final:', sumar_mano(mano))
    return sumar_mano(mano)

# Jugar una partida
while True:
    resultado = jugar_mano()
    if resultado == -1:
        print('Has perdido.')
    elif resultado == 21:
        print('Has ganado.')
    else:
        print('El crupier juega.')
        mano_crupier = []
        mano_crupier.append(repartir_carta())
        mano_crupier.append(repartir_carta())
        while sumar_mano(mano_crupier) < 17:
            mano_crupier.append(repartir_carta())
        print('Mano del crupier:', [carta[0] for carta in mano_crupier])
        print('Suma de la mano del crupier:', sumar_mano(mano_crupier))
        if sumar_mano(mano_crupier) > 21:
            print('El crupier se ha pasado de 21. Ganaste.')
        elif sumar_mano(mano_crupier) >= resultado:
            print('El crupier gana.')
        else:
            print('Has ganado.')
    respuesta = input('¿Quieres jugar otra partida? (s/n): ')
    if respuesta != 's':
        break