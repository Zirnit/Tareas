def decodificar(mensaje):
    binario = mensaje.split(",")
    listaDecimal = []
    for i in binario:
        listaDecimal.append(BinarioADecimal(i))
    listaLetras = []
    for i in listaDecimal:
        listaLetras.append(chr(i))
    mensaje = "".join(listaLetras)
    return mensaje

def BinarioADecimal(textoBin):
    decimal = 0
    for i, j in enumerate(textoBin):
        decimal += int(j)*(2**(len(textoBin)-(i+1)))
    return decimal

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
