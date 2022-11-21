def alineamiento(string1, string2):
    listaSTR1 = []
    lsitaSTR2 = []
    for i in string1:
        listaSTR1.append(i)
    for j in string2:
        lsitaSTR2.append(j)
    for x, y in enumerate(listaSTR1):
        if lsitaSTR2[x] == y:
            pass
        else:
            lsitaSTR2.insert(x,"_")
    respuesta = "".join(lsitaSTR2)
    print(respuesta)

cadena1 = input()
cadena2 = input()

alineamiento(cadena1, cadena2)
