class TarjetaPrepago():
    """docstring for TarjetaPrepago"""

    def __init__(self, numeroTelefono, nif, saldo):

        self.numeroTelefono = str(numeroTelefono)
        self.saldo = float(saldo)
        self.nif = str(nif)
        self.consumo = 0

    def getSaldoActual(self):
        return self.saldo

    def getNif(self):
        return self.nif

    def getConsultarTelefono(self):
        return self.numeroTelefono

    def getConsultarTarjeta(self):
        print("Tú saldo actual es de %s€, tu DNI es %s tu número de telefono es %s y has consumido un total de %s" % (self.getSaldoActual(),self.getNif(), self.getConsultarTelefono(),self.consumo))

    def setrealizarLlamada(self, segundos_hablados):
        self.saldo -= (segundos_hablados+15)/100

        if segundos_hablados <60:
        	self.consumo= str(segundos_hablados) + " Segundos"
        elif segundos_hablados <3600:
        	self.consumo = str(round(segundos_hablados/60,1)) + " Minutos"
        else:
        	self.consumo= str(round(segundos_hablados/600,2)) + " Horas"


    def setingresarSaldo(self, añadir_saldo):
        self.saldo += añadir_saldo

    def setenviarMensaje(self, mensajes):

        self.saldo -= mensajes*9/100


    def __repr__(self):
        return getConsultarTarjeta()


if __name__ == '__main__':

    tarjeta = TarjetaPrepago("61481248", "431325462S", 20)
    tarjeta.setenviarMensaje(5)
    assert tarjeta.getSaldoActual() == 19.55
    tarjeta.setingresarSaldo(40)
    assert tarjeta.getSaldoActual() == 59.55
    tarjeta.setrealizarLlamada(3700)
    assert tarjeta.getSaldoActual() == 22.40
    tarjeta.getConsultarTarjeta()
