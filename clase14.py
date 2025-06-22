class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print("El deposito es de: ", cantidad)

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
             self.saldo -= cantidad
        else:
            print("Saldo insufisiente")
    def mostrar_saldo(self):
        print("El saldo actual es:", self.saldo)
        
    
usuario_uno = CuentaBancaria(500)
usuario_dos = CuentaBancaria(2000)

usuario_uno.depositar(100)
usuario_dos.depositar(400)

usuario_uno.mostrar_saldo()
usuario_dos.mostrar_saldo()

usuario_uno.retirar(150)
usuario_dos.retirar(280)

usuario_uno.mostrar_saldo()
usuario_dos.mostrar_saldo()


    