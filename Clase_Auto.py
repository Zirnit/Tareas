class Auto:

    kilometraje = 0
    cuenta_kilometros = 0
    nivel_estanque = 0

    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_viaje):
        km_recorridos = velocidad * tiempo_viaje
        km_restantes = 0
        autonomia = self.autonomia()
        if autonomia < km_recorridos:
            km_restantes = km_recorridos - autonomia
            km_recorridos = autonomia
        self.cuenta_kilometros += km_recorridos
        self.kilometraje += self.cuenta_kilometros
        self.nivel_estanque -= km_recorridos/self.rendimiento
        return km_restantes

    def autonomia(self):
        km_restantes = self.rendimiento * self.nivel_estanque
        return km_restantes

    def llenar_estanque(self, cantidad_litros):
        litros_totales = self.nivel_estanque + cantidad_litros
        if litros_totales > self.capacidad_estanque:
            return tuple([self.capacidad_estanque, False])
        else:
            self.nivel_estanque = litros_totales
            return tuple([self.nivel_estanque, True])

if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto.autonomia())
    auto.llenar_estanque(10)
    print(auto.autonomia())
