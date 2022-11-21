class FechaHora:
    def __init__(self):
        self.dd = ""
        self.mm = ""
        self.aaaa = ""
        self.HH = ""
        self.MM = ""
        self.SS = ""

    def __str__(self):
        #return f"{self.aaaa}/{self.mm}/{self.dd} {self.HH}:{self.MM}:{self.SS}"
        return self.aaaa + "/" + self.mm + "/" + self.dd + " " + self.HH + ":" + self.MM + ":" + self.SS

    def fijarFecha(self,fecha):
        dia = int(fecha[0:2])
        mes = int(fecha[3:5])
        if dia < 1 or dia > 31 or mes < 1 or mes >12:
            print("Fecha inválida")
            return False
        self.dd = fecha[0:2]
        self.mm = fecha[3:5]
        self.aaaa = fecha[6:10]

    def fijarHora(self,hora):
        hor = int(hora[0:2])
        minuto = int(hora[3:5])
        segundo = int(hora[6:8])
        if hor < 0 or hor > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59:
            return False
        self.HH = hora[0:2]
        self.MM = hora[3:5]
        self.SS = hora[6:8]

    def fijarFechaHora(self,fechahora):
        fecha = fechahora[0:10]
        hora = fechahora[11:19]
        self.fijarFecha(fecha)
        self.fijarHora(hora)

    def cambiar(self,parte):
        parte = parte.replace(" ","")
        indice = parte.find("=")
        par = parte[0:indice]
        teint = int(parte[indice+1:])
        testr = parte[indice+1:]
        if par == "aaaa":
            self.aaaa = testr
        elif par == "mm" and teint >= 1 and teint <= 12:
            self.mm = testr
        elif par == "dd" and teint >= 1 and teint <= 31:
            self.dd = testr
        elif par == "HH" and teint >= 0 and teint <= 23:
            self.HH = testr
        elif par == "MM" and teint >= 0 and teint <= 59:
            self.MM = testr
        elif par == "SS" and teint >= 0 and teint <= 59:
            self.SS = testr
        else:
            print("Error, el valor está fuera de rango")

if __name__ == "__main__":
    fh=FechaHora()
    fh.fijarFechaHora("30-09-2015 17:45:00")
    print(fh)

    fh.cambiar("mm=10")
    print(fh)

    fh.fijarHora("18:00:00")
    fh.cambiar("aaaa = 2016")
    print(fh)
           
