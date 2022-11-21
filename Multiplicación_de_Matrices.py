class Matriz:
    def __init__(self,celdas=[]):
        self.celdas=celdas

    def __repr__(self):
        s=""
        for i in range(len(self.celdas)):
            for j in range(len(self.celdas)):
                s+="{0: >5} ".format(self.celdas[i][j])
            s+="\n"
        return s

    def __mul__(self, otro):
        resultado = [[0]*len(i) for i in self.celdas]
        for i in range(len(self.celdas)):
           for j in range(len(otro.celdas[0])):
               for k in range(len(otro.celdas)):
                  resultado[i][j] += self.celdas[i][k] * otro.celdas[k][j]
        return Matriz(resultado)

if __name__ == "__main__":
    a=Matriz([[9,7,3],[4,2,6],[7,8,15]])
    print(a.celdas)
    b=Matriz([[5,7,1],[6,0,3],[4,9,3]])
    print(b.celdas)
    r=a*b
    print(r)
           
