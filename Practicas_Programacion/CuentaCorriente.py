class CuentaCorriente():

	def __init__(self, nombre, apellidos, direccion, telefono, dni):
		self.__nombre=nombre
		self.__apellidos=str(apellidos)
		self.__direccion=str(direccion)
		self.__telefono=str(telefono)
		self.__saldo= float(1000)
		self.__dni=str(dni)



	def setRetirarDinero(self, dineroretirado):

		self.__saldo-=int(dineroretirado)

		


	def setIngresarDinero(self,dineroingresado):

		self.__saldo+=int(dineroingresado)


	def getNombre(self):

		return self.__nombre

	def getApellidos(self):

		return self.__apellidos

	def getDireccion(self):

		return self.__direccion

	def getTelefono(self):

		return self.__telefono

	def getSaldo(self):

		return self.__saldo
		


	def consultarCuenta(self):
		
		print( "Nombre: " , self.getNombre(), "\nApellidos: ", self.getApellidos(),"\nDireccion: ", self.getDireccion(), "\nTelefono: ", self.getTelefono(),"\nSaldo: ", self.getSaldo())


		

	def saldoNegativo(self):
		

		if self.__saldo >0:
			return False
		else:
			return True

miCuentaCorriente=CuentaCorriente("Marcos","Monjon M","Cfemenias","61722222","3724712s")

if __name__ == "__main__":

	miCuentaCorriente.setIngresarDinero(100)
	assert miCuentaCorriente.getSaldo() == 1100.0
	miCuentaCorriente.setRetirarDinero(400)
	assert miCuentaCorriente.getSaldo()
	assert miCuentaCorriente.saldoNegativo() == False
	miCuentaCorriente.setRetirarDinero(800)
	assert miCuentaCorriente.getSaldo() == -100.00
	assert miCuentaCorriente.saldoNegativo() == True
	assert miCuentaCorriente.getNombre() == "Marcos"
	assert miCuentaCorriente.getSaldo() == -100.0





