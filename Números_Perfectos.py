def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    print(suma)
    if suma == numero:
        return True
    else:
        return False
