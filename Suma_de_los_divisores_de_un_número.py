# completa el código de la función
def suma_divisores(numero):
    divisores = 0
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            divisores +=1
            suma += i
    if divisores == 1:
        return (suma, True)
    else:
        return (suma, False)
