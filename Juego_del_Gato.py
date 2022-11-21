import copy

class JuegoDelGato:

    tablero = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    def __init__(self):
        self.gato = 1   # Jugador
        self.raton = -1 # Computador

    def ganara(self, copiaT, turno):
        return((copiaT[0][0] == turno and copiaT[0][1] == turno and copiaT[0][2] == turno) or
            (copiaT[1][0] == turno and copiaT[1][1] == turno and copiaT[1][2] == turno) or
            (copiaT[2][0] == turno and copiaT[2][1] == turno and copiaT[2][2] == turno) or
            (copiaT[0][0] == turno and copiaT[1][0] == turno and copiaT[2][0] == turno) or
            (copiaT[0][1] == turno and copiaT[1][1] == turno and copiaT[2][1] == turno) or
            (copiaT[0][2] == turno and copiaT[1][2] == turno and copiaT[2][2] == turno) or
            (copiaT[0][0] == turno and copiaT[1][1] == turno and copiaT[2][2] == turno) or
            (copiaT[0][2] == turno and copiaT[1][1] == turno and copiaT[2][0] == turno))

    def __repr__(self):
        tb = self.tablero
        #return f"{self.tablero[0][0]} {self.tablero[0][1]} {self.tablero[0][2]}\n{self.tablero[1][0]} {self.tablero[1][1]} {self.tablero[1][2]}\n{self.tablero[2][0]} {self.tablero[2][1]} {self.tablero[2][2]}"
        return "%d %d %d\n%d %d %d\n%d %d %d" %(tb[0][0],tb[0][1],tb[0][2],tb[1][0],tb[1][1],tb[1][2],tb[2][0],tb[2][1],tb[2][2])

    def jugarGato(self,fila,columna):
        if self.tablero[fila][columna] == 0:
            self.tablero[fila][columna] = self.gato
            return True
        else:
            return False

    def jugarRaton(self):
        for linea in range(0,3): # Trata de ganar
            for columna in range(0,3):
                copiaTablero = copy.deepcopy(self.tablero)
                if copiaTablero[linea][columna] == 0:
                    copiaTablero[linea][columna] = -1
                    if self.ganara(copiaTablero, -1):
                        self.tablero[linea][columna] = -1
                        return True
        for linea in range(0,3): # Trata de evitar que el jugador gane
            for columna in range(0,3):
                copiaTablero = copy.deepcopy(self.tablero)
                if copiaTablero[linea][columna] == 0:
                    copiaTablero[linea][columna] = 1
                    print(copiaTablero)
                    if self.ganara(copiaTablero, 1):
                        self.tablero[linea][columna] = -1
                        return True
        for linea in range(0,3): # Juega la primera casilla vacía
            for columna in range(0,3):
                copiaTablero = copy.deepcopy(self.tablero)
                if copiaTablero[linea][columna] == 0:
                    self.tablero[linea][columna] = -1
                    return True
        return False

    def indicarEstado(self):
        for i in self.tablero:
            if 0 in i:
                jugadas = True
                break
        if self.ganara(self.tablero,1):
            return 2
        elif self.ganara(self.tablero,-1):
            return 3
        elif jugadas:
            return 0
        else:
            return 1

    def cargar_tablero(self,tablero):
        self.tablero = tablero

    def mostrar_tablero(self):
        tb = self.tablero
        return tb


if __name__ == "__main__":
    juego=JuegoDelGato()
    while juego.indicarEstado()==0:
        print("A")
        print(juego)
        x,y=tuple(input("Ingresa tu jugada: ").split(","))
        juego.jugarGato(int(x),int(y))
        juego.jugarRaton()
    print(juego)
         
