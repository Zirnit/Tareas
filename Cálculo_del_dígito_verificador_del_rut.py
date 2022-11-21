#Cálculo del dígito verificador de un rut

rut = int(input("Ingrese un numero sin digito verificador: "))
mult = [2, 3, 4, 5, 6, 7]
def rut_alreves(numero):
    numero = str(numero)
    return numero[::-1]
def valida_rut(nrut):
    nrut = rut_alreves(nrut)
    i=-6
    suma = 0
    for x in nrut:
        suma = suma + int(x) * mult[i]
        i = i + 1
    modulo = suma % 11
    resultado = 11 - modulo
    if resultado == 11:
        dv = 0
    elif resultado == 10:
        dv = "K"
    else:
        dv = resultado
    return dv
print("dv=" + str(valida_rut(rut)))
