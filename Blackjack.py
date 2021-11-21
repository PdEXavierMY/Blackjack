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

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("3\ Black Jack")
lista_cartas = list(cartas)

print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += cartas[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", score)

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))

def valor_de_carta(carta):
    if carta == 1:
        carta = chr(0x1f0a1)
        valorcarta = 11
    if carta == 2:
        carta = chr(0x1f0a2)
        valorcarta = 2
    if carta == 3:
        carta = chr(0x1f0a3)
        valorcarta = 3
    if carta == 4:
        carta = chr(0x1f0a4)
        valorcarta = 4
    if carta == 5:
        carta = chr(0x1f0a5)
        valorcarta = 5
    if carta == 6:
        carta = chr(0x1f0a6)
        valorcarta = 6
    if carta == 7:
        carta = chr(0x1f0a7)
        valorcarta = 7
    if carta == 8:
        carta = chr(0x1f0a8)
        valorcarta = 8
    if carta == 9:
        carta = chr(0x1f0a9)
        valorcarta = 9
    if carta == 10:
        carta = chr(0x1f0aa)
        valorcarta = 10
    if carta == 11:
        carta = chr(0x1f0ab)
        valorcarta = 10
    if carta == 12:
        carta = chr(0x1f0ad)
        valorcarta = 10
    if carta == 13:
        carta = chr(0x1f0ae)
        valorcarta = 10
    return carta, valorcarta

def mano():
    mano = []
    for i in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        valor_de_carta(carta)
        mano.append(carta)
    return mano