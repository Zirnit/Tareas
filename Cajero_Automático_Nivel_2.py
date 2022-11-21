#Cajero Automático

usuario = "10334151"
clave = "1803"
autenticacion = False
saldo = 1000000
saldo_cliente = 100000
billetes20 = [20000, 20]
billetes10 = [10000, 40]
billetes5 = [5000, 40]
print("Bienvenido al cajero. Si desea salir, escriba 'N'")


def user_auth():
    intentos = 2
    user = input("Ingrese su usuario: ")
    while user != usuario:
        user = input("Usuario no registrado, intente nuevamente.")
        if user == "Y":
            break
    contrasena = input("Ingrese su clave: ")
    while contrasena != clave:
        contrasena = input("Clave invalida, le quedan "+ str(intentos) + " intentos")
        intentos = intentos -1
        if contrasena == "Y":
            break
        if intentos == 0:
            print("tarjeta bloqueada")
            break
    if user == usuario and contrasena == clave:
        autenticacion = True
        return autenticacion

def user_retiro():
    global saldo
    global saldo_cliente
    global billetes20
    global billetes10
    global billetes5
    ret_bill = 0
    while True:
        retiro = input("Ingrese el monto a retirar, este cajero solo da multiplos de 5000: ")
        if retiro == "Y":
            break
        elif int(retiro) > saldo_cliente or int(retiro)%5000 > 0:
            print("Monto no permitido")
        else:
            retiro = int(retiro)
            saldo_cliente = saldo_cliente - retiro
            saldo = saldo - retiro
            while ret_bill < retiro:
                if retiro-ret_bill >= 20000:
                    billetes20[1] = billetes20[1] - int((retiro-ret_bill)/20000)
                    ret_bill = int((retiro-ret_bill)/20000)*20000 + ret_bill
                elif retiro-ret_bill >= 10000:
                    billetes10[1] = billetes10[1] - int((retiro-ret_bill)/10000)
                    ret_bill = int((retiro-ret_bill)/10000) * 10000 + ret_bill
                else:
                    billetes5[1] = billetes5[1] - int((retiro-ret_bill)/5000)
                    ret_bill = int((retiro-ret_bill)/5000) * 5000 + ret_bill          

user_auth()
user_retiro()
print("saldo cuenta=" + str(saldo_cliente))
print("saldo cajero="+ str(saldo))
print("billetes 20000="+str(20-billetes20[1]))
print("billetes 10000="+str(40-billetes10[1]))
print("billetes 5000="+str(40-billetes5[1]))
