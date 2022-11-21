import re
from unicodedata import numeric

palabrasRegex = re.compile(r"\w+")
caracteresRegex = re.compile(r".",re.DOTALL)
espaciosRegex = re.compile(r" ")
puntuacionRegex = re.compile(r"\.|\,|\:|\;")

hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(frase):
    numPalabras = len(palabrasRegex.findall(frase))
    numCaracteres = len(caracteresRegex.findall(frase))
    numEspacios = len(espaciosRegex.findall(frase))
    numPuntuacion = len(puntuacionRegex.findall(frase))
    letras = 0
    for i in palabrasRegex.findall(frase):
        letras += len(i)
    largoPromedio = letras/numPalabras
    #print(f"Palabras: {numPalabras}\nCaracteres: {numCaracteres}\nEspacios: {numEspacios}\nPuntuacion: {numPuntuacion}\nPromedio palabra: {largoPromedio}")
