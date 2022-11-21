import random

def ocultar_letras(palabra,cantidad):
    palabra_lista = []
    j = 0
    for i in palabra:
        palabra_lista.append(i)
    while j < cantidad:
        aleatorio = random.randrange(0, len(palabra_lista))
        if palabra_lista[aleatorio] == "_":
            j-= 1
        palabra_lista[aleatorio] = "_"
        j += 1
    palabra = "".join(palabra_lista)
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    palabra_lista2 = []
    for i in palabra:
        palabra_lista2.append(i)
    for x, y in enumerate(palabra_secreta):
            if letra == y:
                palabra_lista2[x] = y
    palabra = "".join(palabra_lista2)
    return palabra
