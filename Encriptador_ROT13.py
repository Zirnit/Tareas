abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def rot13(palabra):
    lista = []
    for i in palabra:
        indice = abecedario.index(i)
        if indice >= 13:
            indice -= 13
        else:
            indice += 13
        lista.append(abecedario[indice])
    palabra = "".join(lista)
    return palabra
