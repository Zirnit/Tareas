import re

letrasRegex = re.compile(r"\w{1}")

def sopaletras(nombre_archivo,palabras) -> tuple:
    archivo = open(nombre_archivo,"r")
    listaLetras = []
    for i in archivo:
        linea = letrasRegex.findall(i)
        listaLetras.append("".join(linea).lower())
    archivo.close()
    posicion = []
    direccion = []
    for j in palabras:
        y, z = encuentraEnSopa(listaLetras, j)
        posicion.append(y)
        direccion.append(z)
    print(palabras)
    print(posicion)
    print(direccion)
    respuesta = []
    for h, l in enumerate(palabras):
        respuesta.append(tuple([palabras[h], posicion[h], direccion[h]]))
    return tuple(respuesta)

def encuentraEnSopa(listaLetras, palabra):
    coordenada = [0, 0]
    direccion = ""

    for i, j in enumerate(listaLetras):
        if palabra in j:
            direccion = "derecha"
            coordenada = [i, palabra.find(j)]
            return coordenada, direccion

    listaVertical = hacerListaVertical(listaLetras)
    for i, j in enumerate(listaVertical):
        if palabra in j:
            direccion = "abajo"
            coordenada = [palabra.find(j), i]
            return coordenada, direccion

    listaDiagonal, listaCoord = hacerListaDyC(listaLetras)
    for i, j in enumerate(listaDiagonal):
        if palabra in j:
            direccion = "diagonal"
            coordenadaAux = [i, palabra.find(j)]
            coordenada = listaCoord[coordenadaAux[0]][coordenadaAux[1]]
            return coordenada, direccion

def hacerListaVertical(listaLetras):
    listaVertical = []
    for x in range(len(listaLetras[0])):
        for y in listaLetras:
            listaVertical.append(y[x])
    lineas = len(listaLetras)
    listaAux = "".join(listaVertical)
    separaRegex = re.compile(r"\w"*lineas)
    listaVertical = separaRegex.findall(listaAux)
    return listaVertical

def hacerListaDyC(listaLetras):
    matrizLetras = []
    matrizCoord = []
    matrizCoordAux = []
    for i in listaLetras:
        matrizLetras.append(letrasRegex.findall(i))
    for m, n in enumerate(listaLetras):
        for o in range(len(n)):
            matrizCoordAux.append([m,o])
        matrizCoord.append(matrizCoordAux.copy())
        matrizCoordAux.clear()
    columnas = len(matrizLetras[0])
    filas = len(matrizLetras)
    listaDiagonal = [[] for _ in range(filas + columnas - 1)]
    listaCoord = [[] for _ in range(filas + columnas - 1)]
    min_bdiag = -filas + 1
    for x in range(columnas):
        for y in range(filas):
            listaDiagonal[x-y-min_bdiag].append(matrizLetras[y][x])
    for j, h in enumerate(listaDiagonal):
        listaDiagonal[j] = "".join(h)
    for x in range(columnas):
        for y in range(filas):
            listaCoord[x-y-min_bdiag].append(matrizCoord[y][x])
    return listaDiagonal, listaCoord

if __name__=="__main__":
    #print(sopaletras("sopa.txt", ["cra"]))
    #print(sopaletras("sopa.txt", ["aro"]))
    #print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt", ["casa","cra","aro"]))
    #print(sopaletras("sopa.txt", ["ioam"]))
    #print(sopaletras("sopa.txt", ["ahm"]))
    ejemplo = sopaletras("sopa.txt", ["casa","cra","aro"])
    print(type(ejemplo))
