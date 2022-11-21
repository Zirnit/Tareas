def buscarTodas(a,b):
    lista = []
    largo = len(a)
    while b in a:
        indice = a.index(b)
        lista.append(str(indice))
        x, y, a = a.partition(b)
        a = a.rjust(largo)
    respuesta = " ".join(lista)
    return respuesta
