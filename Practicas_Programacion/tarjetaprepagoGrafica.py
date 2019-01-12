
from tkinter import *
from tkinter import ttk


class TarjetaPrepago():
    """docstring for TarjetaPrepago"""

    def __init__(self):
        self.raiz = Tk()
        self.ingresar = IntVar()
        self.ingresardni = StringVar()
        self.dni = ""
        self.ingresarNumero = StringVar()
        self.numeroTelefono = ""
        self.saldo = float(0)
        self.consumo = 0

        self.etiq3 = ttk.Label(self.raiz,text="¿Cuanto quieres ingresar?")

        self.dist = ttk.Entry(self.raiz, textvariable=self.ingresar,width=10)

        self.etiq4 = ttk.Label(self.raiz,text="Introduce tu DNI")

        self.dist1 = ttk.Entry(self.raiz, textvariable=self.ingresardni,width=10)

        self.etiq4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist1.pack(side=TOP, fill=X, expand=True,padx=20, pady=5)

        self.etiq5 = ttk.Label(self.raiz,text="Introduce tu Telefono")

        self.dist2 = ttk.Entry(self.raiz, textvariable=self.ingresarNumero,width=10)

        self.etiq5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist2.pack(side=TOP, fill=X, expand=True,padx=20, pady=5)

        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

        self.dist.pack(side=TOP, fill=X, expand=True,padx=20, pady=5)

        self.boton1 = ttk.Button(self.raiz, text="Ingresar",command=self.setingresarSaldo)

        self.boton1.pack(side=LEFT, fill=BOTH, expand=True,padx=10, pady=10)

        self.printButton = Button(self.raiz, text="Datos de la cuenta", command=self.getConsultarTarjeta)

        self.printButton.pack(side=RIGHT)

        self.printButton1 = Button(self.raiz, text="Introducir DNI", command=self.setNif)

        self.printButton1.pack(side=RIGHT)

        self.printButton2 = Button(self.raiz, text="Introducir Telefono", command=self.setTelefono)

        self.printButton2.pack(side=RIGHT)

        self.raiz.mainloop()

    def getSaldoActual(self):
        return self.saldo

    def getNif(self):
        return self.dni

    def getConsultarTelefono(self):
        return self.numeroTelefono

    def getConsultarTarjeta(self):
        print("Tú saldo actual es de %s€, tu DNI es %s tu número de telefono es %s y has consumido un total de %s" % (
            self.getSaldoActual(), self.getNif(), self.getConsultarTelefono(), self.consumo))

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

    def setrealizarLlamada(self, segundos_hablados):
        self.saldo -= (segundos_hablados+15)/100

        if segundos_hablados < 60:
            self.consumo = str(segundos_hablados) + " Segundos"
        elif segundos_hablados < 3600:
            self.consumo = str(round(segundos_hablados/60, 1)) + " Minutos"
        else:
            self.consumo = str(round(segundos_hablados/600, 2)) + " Horas"

    def setingresarSaldo(self):

        self.setSaldo(self.ingresar.get())

    def setenviarMensaje(self, mensajes):

        self.saldo -= mensajes*9/100

    def __repr__(self):
        return getConsultarTarjeta()


def main():
    mi_app = TarjetaPrepago()
    return 0


if __name__ == '__main__':
    main()


