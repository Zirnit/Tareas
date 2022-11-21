#Cajero Automático

saldo = 1000000
saldo_cliente = 100000
usuario = "10334151"
clave = "1803"
autenticacion = False
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
    global saldo_cliente
    global saldo
    while True:
        retiro = input("Ingrese el monto a retirar: ")
        if retiro == "Y":
            break
        elif int(retiro) > saldo_cliente:
            print("Monto no permitido")
        else:
            saldo_cliente = saldo_cliente - int(retiro)
            saldo = saldo - int(retiro)
            

user_auth()
user_retiro()
print("saldo cuenta=" + str(saldo_cliente))
print("saldo cajero="+ str(saldo))
