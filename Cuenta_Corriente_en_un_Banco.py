class Cuenta:
    def __init__(self, rut, saldo) -> None:
        self.rut = rut
        self.saldo = saldo

    def girar(self, monto):
        if monto > self.saldo:
            return False
        else:
            self.saldo -= monto
            return True
