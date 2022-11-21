# completa el código de la función
def amigos(a,b):
    suma1 = 0
    suma2 = 0
    for x in range(2, a+1):
        if int(a) % x == 0:
            suma1 = suma1 + a/x
    for x in range(2, b+1):
        if int(b) % x == 0:
            suma2 = suma2 + b/x
    if suma1 == int(b) and suma2 == int(a):
        return True
    else:
        return False
