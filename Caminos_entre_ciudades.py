class Ciudad:
    puntos = []

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.puntos.append([p1, p2])

    def camino(self, other):
        return (self.puntos)

    def distancia(self, other):
        dist = ((self.p1-other.p1)**2+(self.p2-other.p2)**2)**0.5
        return dist
