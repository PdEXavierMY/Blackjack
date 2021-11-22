import random
from pedir_numero import (pedir_entrada_numero, pedir_entrada_numero_delimitado)

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

def simbolo_carta(carta):
    if carta == 1:
        carta = chr(0x1f0a1)
    elif carta == 2:
        carta = chr(0x1f0a2)
    elif carta == 3:
        carta = chr(0x1f0a3)
    elif carta == 4:
        carta = chr(0x1f0a4)
    elif carta == 5:
        carta = chr(0x1f0a5)
    elif carta == 6:
        carta = chr(0x1f0a6)
    elif carta == 7:
        carta = chr(0x1f0a7)
    elif carta == 8:
        carta = chr(0x1f0a8)
    elif carta == 9:
        carta = chr(0x1f0a9)
    elif carta == 10:
        carta = chr(0x1f0aa)
    elif carta == 11:
        carta = chr(0x1f0ab)
    elif carta == 12:
        carta = chr(0x1f0ad)
    else:
        carta = chr(0x1f0ae)
    return carta

def puntuacion(carta, total):
    if carta == 1:
        total += 11
    elif carta == 2:
        total += 2
    elif carta == 3:
        total += 3
    elif carta == 4:
        total += 4
    elif carta == 5:
        total += 5
    elif carta == 6:
        total += 6
    elif carta == 7:
        total += 7
    elif carta == 8:
        total += 8
    elif carta == 9:
        total += 9
    elif carta == 10:
        total += 10
    elif carta == 11:
        total += 10
    elif carta == 12:
        total += 10
    elif carta == 13:
        total += 10
    return total

def carta_inicial(baraja):
    mano = []
    total = 0
    for i in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        puntos = puntuacion(carta, 0)
        total += puntos
        carta = simbolo_carta(carta)
        mano.append(carta)
    return mano, total

def pedir_carta(mano):
    total = list(carta_inicial(baraja)).pop()
    print(total)
    carta = baraja.pop()
    puntos = puntuacion(carta, total)
    total += puntos
    carta = simbolo_carta(carta)
    mano.append(carta)
    return mano, total

def resultados(jugador, banca):
    print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
    print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")

def partida(jugador, banca):
    if jugador[1] == 21:
        resultados(jugador, banca)
        print("Tienes un blackjack!!!, Has ganado!!!")
    if jugador[1] > 21:
        resultados(jugador, banca)
        print("Te has pasado de 21, has perdido.")
    if jugador[1] < banca[1]:
        resultados(jugador, banca)
        print("Has perdido, la banca tiene más puntos.")
    if jugador[1] > banca[1]:
        resultados(jugador, banca)
        print("Has ganado a la banca!!!")
    if banca[1] == 21:
        resultados(jugador, banca)
        print("Has perdido :(, la banca tiene un blackjack")
    if banca[1] > 21:
        resultados(jugador, banca)
        print("La banca se ha pasado, tú ganas.")

def jugar_de_nuevo():
    otra = pedir_entrada_numero_delimitado("¿Quieres jugar de nuevo?: Sí=1, No=2", 1, 2)
    if otra == 1:
        jugador = []
        banca = []
        baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
        juego()
    else:
        print("Gracias por jugar.")

  
def juego():
    opcion = 0
    print("Vamos a jugar Blackjack!!!")
    jugador = list(carta_inicial(baraja))
    banca = list(carta_inicial(baraja))
    if banca[1] == 21:
        print("La banca ha sacado un blackjack, por lo que pierdes.")
        jugar_de_nuevo()
    elif jugador[1] == 21:
        print("Has sacado un blackjack!!!, se acabó el juego.")
        jugar_de_nuevo()
    else:
        while opcion != 3:
            print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
            print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")
            opcion = pedir_entrada_numero_delimitado("¿Quieres coger carta(1), plantarte(2) o acabar(3)?", 1, 3)
            if opcion == 1:
                pedir_carta(jugador[0])
                while puntuacion(banca[0], banca[1]) < 16:
                    pedir_carta(banca[0])
                partida(jugador, banca)
                jugar_de_nuevo()
            if opcion == 2:
                while puntuacion(banca[0], banca[1]) < 16:
                    pedir_carta(banca[0])
                partida(jugador, banca)
                jugar_de_nuevo()
            if opcion == 3:
                print("Gracias por jugar")
                break

juego()