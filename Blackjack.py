import random
from random import choice, sample

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

def valor_de_carta(carta):
    total = 0
    if carta == 1:
        carta = chr(0x1f0a1)
        total += 11
    elif carta == 2:
        carta = chr(0x1f0a2)
        total += 2
    elif carta == 3:
        carta = chr(0x1f0a3)
        total += 3
    elif carta == 4:
        carta = chr(0x1f0a4)
        total += 4
    elif carta == 5:
        carta = chr(0x1f0a5)
        total += 5
    elif carta == 6:
        carta = chr(0x1f0a6)
        total += 6
    elif carta == 7:
        carta = chr(0x1f0a7)
        total += 7
    elif carta == 8:
        carta = chr(0x1f0a8)
        total += 8
    elif carta == 9:
        carta = chr(0x1f0a9)
        total += 9
    elif carta == 10:
        carta = chr(0x1f0aa)
        total += 10
    elif carta == 11:
        carta = chr(0x1f0ab)
        total += 10
    elif carta == 12:
        carta = chr(0x1f0ad)
        total += 10
    elif carta == 13:
        carta = chr(0x1f0ae)
        total += 10
    return carta, total

def carta_inicial():
    mano = []
    for i in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        valor_de_carta(carta)
        mano.append(carta)
        print(mano)
    return mano