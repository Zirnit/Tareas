#Juego adivina mi número

from random import randrange
numero = randrange(20)+1
x = 0
while True:
    if x == 5:
        print("No adivinaste, mi numero era " + str(numero))
        break
    intento = 1
    if intento > numero:
        print("mi numero es menor")
    elif intento < numero:
        print("mi numero es mayor")
    else:
        print("Adivinaste, mi numero era " + str(numero))
        break
    x = x + 1
