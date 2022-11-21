#Descomponer un número

numero = input("Ingrese un numero de hasta 4 digitos: ")
if len(numero) == 4:
    descomposicion = numero[0] + "M + " + numero[1] + "C + " + numero[2] + "D + " + numero[3] + "U"
elif len(numero) == 3:
    descomposicion = numero[0] + "C + " + numero[1] + "D + " + numero[2] + "U"
elif len(numero) == 2:
    descomposicion = numero[0] + "D + " + numero[1] + "U"
else:
    descomposicion = numero + "U"
print(descomposicion)
