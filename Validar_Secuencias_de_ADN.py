import re

adnRegex = re.compile(r"A|C|T|G")

def validaSecuencia(string):
    string = string.upper()
    listaADN = adnRegex.findall(string)
    cadenaADN = "".join(listaADN)
    if cadenaADN == string:
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")
        
cadena = input()
validaSecuencia(cadena)
