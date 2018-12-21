class Vehiculos():

	def __init__(self, marca, modelo):

		self.marca = marca
		self.modelo = modelo
		self.enmarcha = False
		self.acelera = False
		self.frena = False


	def arrancar(self):

		self.enmarcha = True

	def acelerar(self):

		self.acelera = True

	def frenar(self):
		
		self.frena = True

	def estado(self):

		print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nEn Marcha ",
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculos):

	def carga(self, cargar):

		self.cargar=cargar

		if(self.cargar):
			return "La furgoneta está cargada"
		else:
			return "La furgoneta no está cargada"


class Moto(Vehiculos):
	pass





class VehiculosElectricos(Vehiculos):


	def __init__(self, marca , modelo):

		super().__init__(marca, modelo)  # Hace que se puedan heredar los parametros del primer constructor
		
		self.autonomia = 100		#|
						#|
	def cargarEnergia(self):		#|
						#|
		self.cargando = True		#|
						#|
						#|	
						#|
						#↓

class BicicletaElectrica(VehiculosElectricos,Vehiculos):   # La herencia múltiple, se le dará preferencia a la clase que tenemos en la primera posición, es decir, VehiculosElectricos
	pass





miMoto=Moto("Kawasaki","Ninja")

miMoto.arrancar()

miMoto.estado()

print(" ---------------------------")
#------------------------------------- Separación de clases de vehiculos

miFurgoneta=Furgoneta("Renault", "Berlingo")

miFurgoneta.estado()

print(miFurgoneta.carga(True))

print("--------------------------")

miBicicleta=BicicletaElectrica("Orbea","CS")

miBicicleta.estado()

