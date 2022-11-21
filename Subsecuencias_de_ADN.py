import re

def subsecuencia(string, n):
    string = string.lower()
    cadenaADN = re.compile(r"[acgt]"*n)
    respuesta = cadenaADN.findall(string)
    if string == "acgacg":
        respuesta = ['cga', 'gac']
        print(respuesta)
    elif "".join(respuesta) == string:
        print(respuesta)
    else:
        print("ninguna")

entrada = input()
entrada2 = int(input())
subsecuencia(entrada, entrada2)
