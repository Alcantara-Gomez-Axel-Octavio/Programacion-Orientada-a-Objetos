class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    def consultar_saldo(self):
        return self.saldo
class Cliente:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = cuenta
    def solicitar_saldo(self):
        saldo_actual = self.cuenta.consultar_saldo()
        print(f"El saldo actual de {self.nombre} es {saldo_actual}.")
# Creamos un objeto de la clase CuentaBancaria y un objeto de la clase Cliente
cuenta1 = CuentaBancaria(1000)
cliente1 = Cliente("Juan", cuenta1)
# El cliente solicita el saldo de su cuenta bancaria
cliente1.solicitar_saldo()  # Imprime "El saldo actual de Juan es 1000."