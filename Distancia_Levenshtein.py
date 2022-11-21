#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales

def levenshtein(palabra1,palabra2):
    listaLevenshtein = [([0]*(len(palabra2)+1)) for i in range(len(palabra1)+1)]
    for p1 in range(len(palabra1) + 1):
        listaLevenshtein[p1][0] = p1
    for p2 in range(len(palabra2) + 1):
        listaLevenshtein[0][p2] = p2
    a = 0
    b = 0
    c = 0
    for p1 in range(1, len(palabra1) + 1):
        for p2 in range(1, len(palabra2) + 1):
            if (palabra1[p1-1] == palabra2[p2-1]):
                listaLevenshtein[p1][p2] = listaLevenshtein[p1 - 1][p2 - 1]
            else:
                a = listaLevenshtein[p1][p2 - 1]
                b = listaLevenshtein[p1 - 1][p2]
                c = listaLevenshtein[p1 - 1][p2 - 1]
                if (a <= b and a <= c):
                    listaLevenshtein[p1][p2] = a + 1
                elif (b <= a and b <= c):
                    listaLevenshtein[p1][p2] = b + 1
                else:
                    listaLevenshtein[p1][p2] = c + 1
    resultado = (listaLevenshtein[len(palabra1)][len(palabra2)])
    if resultado == 0:
        return "0D"
    elif resultado > 1:
        return "+1"
    elif len(palabra1) != len(palabra2):
        return "IB"
    else:
        return "1S"

if __name__=="__main__":
    levenshtein("12345", "123")
