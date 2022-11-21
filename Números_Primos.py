# por favor escribe aquí tu función
def es_primo(numero):
    cuenta = 0
    for i in range(1, numero+1):
        if (numero % i) == 0:
            cuenta = cuenta + 1
        i = i + 1
    if cuenta == 2:
        return True
    else:
        return False
