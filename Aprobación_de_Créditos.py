#Aprobación de créditos

ingreso = int(input("Ingrese sus ingresos en pesos: "))
nacimiento = int(input("Ingrese su anho de nacimiento: "))
NHijos = int(input("Ingrese la cantidad de hijos que tiene: "))
anhosBanco = int(input("Ingrese la cantidad de anhos que ha estado en el banco: "))
ECivil = input("Ingrese su estado civil\n'S': soltero, 'C': casado ")
vivienda = input("Ingrese si vive en campo o ciudad\n'U': urbano, 'R': rural ")

edad = 2022 - nacimiento
aprobacion = "APROBADO"

if anhosBanco > 10 and NHijos >=2:
    aprobacion = "APROBADO"
elif ECivil == "C" and NHijos >= 3 and 45<=edad<=55:
    aprobacion = "APROBADO"
elif ingreso > 2500000 and ECivil == "S" and vivienda == "U":
    aprobacion = "APROBADO"
elif ingreso > 3500000 and anhosBanco > 5:
    aprobacion = "APROBADO"
elif vivienda == "R" and ECivil == "C" and NHijos < 2:
    aprobacion = "APROBADO"
else:
    aprobacion = "RECHAZADO"
print(aprobacion)
