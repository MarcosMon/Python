
from tkinter import *


class TarjetaPrepago():
    """docstring for TarjetaPrepago"""

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Tarjeta prepago Orange")
        self.raiz.config(bg="Yellow")
        self.ingresar = IntVar()
        self.ingresardni = StringVar()
        self.dni = ""
        self.ingresarNumero = StringVar()
        self.numeroTelefono = ""
        self.saldo = float(0)
        self.consumo = 0
        self.consumoLlamadas = 0
        self.consumoMensajes = 0
        self.tiempoHablado = 0

        self.etiq3 = Label(self.raiz, text="¿Cuanto quieres ingresar?", background="orange")

        self.dist = Entry(self.raiz, textvariable=self.ingresar, width=10,justify="center")

        self.etiq4 = Label(self.raiz, text="Introduce tu DNI",background="orange")

        self.dist1 = Entry(
            self.raiz, textvariable=self.ingresardni, width=10,justify="center")

        self.etiq4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist1.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.etiq5 = Label(self.raiz, text="Introduce tu Telefono",background="orange")

        self.dist2 = Entry(
            self.raiz, textvariable=self.ingresarNumero, width=10,justify="center")

        self.etiq5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist2.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

        self.boton1 = Button(
            self.raiz, text="Ingresar", command=self.ingresarSaldo,background="orange")

        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        self.printButton = Button(
            self.raiz, text="Datos de la cuenta", command=self.consultarTarjeta,background="orange")

        self.printButton.pack(side=RIGHT)

        self.printButton1 = Button(
            self.raiz, text="Introducir DNI", command=self.setNif,background="orange")

        self.printButton1.pack(side=RIGHT)

        self.printButton2 = Button(
            self.raiz, text="Introducir Telefono", command=self.setTelefono,background="orange")

        self.printButton2.pack(side=RIGHT)

        self.raiz.mainloop()

    def getSaldo(self):
        return self.saldo


    def getDni(self):
        return self.dni


    def getTelefono(self):
        return self.numeroTelefono


    def getHora(self):
        return self.tiempoHablado


    def getConsumoLlamadas(self):
        return self.consumoLlamadas


    def getConsumoMensajes(self):
        return self.consumoMensajes


    def setConsumoLLamadas(self, gastos):
        self.consumoLlamadas += gastos


    def setConsumoMensajes(self, gastos):
        self.consumoMensajes += gastos


    def setHora(self, tiempoHablado):
        if tiempoHablado < 60:
            self.tiempoHablado = str(tiempoHablado) + " Segundos"
        elif tiempoHablado < 3600:
            self.tiempoHablado = str(round(tiempoHablado/60, 1)) + " Minutos"
        else:
            self.tiempoHablado = str(round(tiempoHablado/600, 2)) + " Horas"


    def setSaldo(self, añadir_saldo):
        self.saldo += añadir_saldo


    def setTelefono(self):
        self.numeroTelefono = self.ingresarNumero.get()

        assert len(self.numeroTelefono) == 9
        assert self.numeroTelefono.isdigit(), "Tiene que ser numérico"

        if self.numeroTelefono.isdigit() and len(self.numeroTelefono) == 9:
            self.numeroTelefono = self.ingresarNumero.get()
        else:
            self.numeroTelefono = "Telefono incorrecto"


    def setNif(self):
        self.dni = self.ingresardni.get()
        if len(self.dni) == 9:
            self.dni = self.ingresardni.get()
        else:
            self.dni = "DNI erróneo"

        assert len(self.ingresardni.get()) == 9, "Tiene que tener 9 caracteres"


    def realizarLlamada(self, segundos_hablados):
        self.setSaldo(-(segundos_hablados + 15) / 100)
        self.setConsumoLLamadas((segundos_hablados+15)/100)
        self.setHora(segundos_hablados)


    def ingresarSaldo(self):
        self.setSaldo(self.ingresar.get())


    def enviarMensaje(self, mensajes):
        self.setSaldo(-(n_mensajes * 9) / 100)
        self.setConsumoMensajes(mensajes*9/100)


    def consultarTarjeta(self):
        print("Tú saldo actual es de %s€, tu DNI es %s tu número de telefono es %s y has consumido un total de %s€ en llamadas y %s€ en mensajes. (Total hablado %s)" % (
            self.getSaldo(), self.getDni(), self.getTelefono(), self.getConsumoLlamadas(), self.getConsumoMensajes(), self.getHora()))


    def __repr__(self):
        return consultarTarjeta()


def main():
    mi_app = TarjetaPrepago()
    return 0


if __name__ == '__main__':
    main()
