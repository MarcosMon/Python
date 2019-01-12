class TarjetaPrepago():
    """docstring for TarjetaPrepago"""

    def __init__(self, numeroTelefono, nif, saldo):

        self.numeroTelefono = str(numeroTelefono)
        self.saldo = float(saldo)
        self.nif = str(nif)
        self.consumoLlamadas = 0
        self.consumoMensajes = 0
        self.tiempoHablado = 0

    def getSaldo(self):
        return round(self.saldo, 2)

    def getNif(self):
        return self.nif

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def getConsultarTarjeta(self):
        print("Tú saldo actual es de %s€, tu DNI es %s tu número de telefono es %s y has consumido un total de %s€ en llamadas y %s€ en mensajes. (Total hablado %s)" % (
            self.getSaldo(), self.getNif(), self.getNumeroTelefono(), self.getConsumoLlamadas(), self.getConsumoMensajes(), self.getHora()))

    def setNif(self):
        self.nif = nif

    def setHora(self, tiempoHablado):
        if tiempoHablado < 60:
            self.tiempoHablado = str(tiempoHablado) + " Segundos"
        elif tiempoHablado < 3600:
            self.tiempoHablado = str(round(tiempoHablado/60, 1)) + " Minutos"
        else:
            self.tiempoHablado = str(round(tiempoHablado/600, 2)) + " Horas"

    def getHora(self):
        return self.tiempoHablado

    def setConsumoLLamadas(self, gastos):
        self.consumoLlamadas += gastos

    def getConsumoLlamadas(self):
        return self.consumoLlamadas

    def setConsumoMensajes(self, gastos):
        self.consumoMensajes += gastos

    def getConsumoMensajes(self):
        return self.consumoMensajes

    def setSaldo(self, gastos):
        self.saldo -= gastos

    def setNumeroTelefono(self):
        self.numeroTelefono = numeroTelefono

    def setrealizarLlamada(self, segundos_hablados):
        self.setSaldo((segundos_hablados+15)/100)
        self.setConsumoLLamadas((segundos_hablados+15)/100)
        self.setHora(segundos_hablados)

    def setingresarSaldo(self, añadir_saldo):
        self.setSaldo(-añadir_saldo)

    def setenviarMensaje(self, mensajes):

        self.setSaldo(mensajes*9/100)
        self.setConsumoMensajes(mensajes*9/100)

    def __repr__(self):
        return getConsultarTarjeta()


if __name__ == '__main__':

    tarjeta = TarjetaPrepago("61481248", "431325462P", 20)
    tarjeta.setenviarMensaje(72)
    assert tarjeta.getSaldo() == 13.52
    tarjeta.setingresarSaldo(40)
    assert tarjeta.getSaldo() == 53.52
    tarjeta.setrealizarLlamada(3700)
    assert tarjeta.getSaldo() == 16.37
    assert tarjeta.getConsumoMensajes() == 6.48
    tarjeta.getConsultarTarjeta()
