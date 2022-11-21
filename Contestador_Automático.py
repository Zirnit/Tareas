#Contestador de celular

num_telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
contestar = "CONTESTAR"

if hora <= 7 and hora >= 0:
    contestar = "CONTESTAR"
elif hora <= 14 and int(str(num_telefono)[-3:]) == 909:
    contestar = "CONTESTAR"
elif hora <= 19 and hora >= 17 and int(str(num_telefono)[:3]) != 877:
    contestar = "CONTESTAR"
else:
    contestar = "NO CONTESTAR"
print(contestar)
