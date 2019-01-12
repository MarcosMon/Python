
from tkinter import *
from tkinter import ttk

class TarjetaPrepago():
    """docstring for TarjetaPrepago"""

    def __init__(self, numeroTelefono, nif, saldo):
        self.raiz = Tk()
        self.ingresar = IntVar()
        self.numeroTelefono = str(numeroTelefono)
        self.saldo = float(saldo)
        self.nif = str(nif)
        self.consumo = 0
        self.etiq3 = ttk.Label(self.raiz, 
                               text="¿Cuanto quieres ingresar?")
        self.dist = ttk.Entry(self.raiz, textvariable=self.ingresar, 
                              width=10)

        self.boton2 = ttk.Button(self.raiz, text="Salir", 
                                 command=quit) 

        self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        
        self.dist.pack(side=TOP, fill=X, expand=True, 
                       padx=20, pady=5)
        self.boton1 = ttk.Button(self.raiz, text="Ingresar", 
                                 command=self.setingresarSaldo)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=10, pady=10)
        self.printButton = Button(self.raiz, text="Datos de la cuenta", command=self.getConsultarTarjeta)
        self.printButton.pack(side=RIGHT)
        self.raiz.mainloop()



    def getSaldoActual(self):
        return self.saldo

    def getNif(self):
        return self.nif

    def getConsultarTelefono(self):
        return self.numeroTelefono

    def getConsultarTarjeta(self):
        print("Tú saldo actual es de %s€, tu DNI es %s tu número de telefono es %s y has consumido un total de %s" % (self.getSaldoActual(),self.getNif(), self.getConsultarTelefono(),self.consumo))

    def setSaldo(self,añadir_saldo):
        self.saldo += añadir_saldo

    def setTelefono(self):
        self.numeroTelefono = numeroTelefono

    def setNif(self):
        self.nif = nif

    def setrealizarLlamada(self, segundos_hablados):
        self.saldo -= (segundos_hablados+15)/100

        if segundos_hablados <60:
        	self.consumo= str(segundos_hablados) + " Segundos"
        elif segundos_hablados <3600:
        	self.consumo = str(round(segundos_hablados/60,1)) + " Minutos"
        else:
        	self.consumo= str(round(segundos_hablados/600,2)) + " Horas"


    def setingresarSaldo(self):

        self.setSaldo(self.ingresar.get())
        
    def setenviarMensaje(self, mensajes):

        self.saldo -= mensajes*9/100


    def __repr__(self):
        return getConsultarTarjeta()




def main():
    mi_app = TarjetaPrepago("61481248", "431325462S", 20)
    mi_app.getConsultarTarjeta()
    return 0

if __name__ == '__main__':
    main()


"""
if __name__ == '__main__':

    tarjeta = TarjetaPrepago("61481248", "431325462S", 20)
    tarjeta.setenviarMensaje(5)
    assert tarjeta.getSaldoActual() == 19.55
    tarjeta.setingresarSaldo(40)
    assert tarjeta.getSaldoActual() == 59.55
    tarjeta.setrealizarLlamada(3700)
    assert tarjeta.getSaldoActual() == 22.40
    tarjeta.getConsultarTarjeta()
"""