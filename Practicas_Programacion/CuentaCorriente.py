class CuentaCorriente():

	def __init__(self, nombre, apellidos, direccion, telefono, dni):
		self.nombre=nombre
		self.apellidos=str(apellidos)
		self.direccion=str(direccion)
		self.telefono=str(telefono)
		self.saldo= float(1000)
		self.dni=str(dni)

	def getNombre(self):

		return self.nombre

	def getApellidos(self):

		return self.apellidos

	def getDireccion(self):

		return self.direccion

	def getTelefono(self):

		return self.telefono

	def getSaldo(self):

		return self.saldo

	def setNombre(self):
		self.nombre = nombre

	def setApellidos(self):
		self.apellidos = apellidos

	def setDireccion(self):
		self.direccion = direccion

	def setTelefono(self):
		self.telefono = telefono

	def setSaldo(self,dinero):
		self.saldo += dinero

	def RetirarDinero(self, dineroretirado):

		self.setSaldo(-dineroretirado)

	def IngresarDinero(self,dineroingresado):

		self.setSaldo(dineroingresado)


	def saldoNegativo(self):

		if self.saldo >0:
			return False
		else:
			return True

	def consultarCuenta(self):
		
		print( "Nombre:" , self.getNombre(), "\nApellidos:", self.getApellidos(),"\nDireccion:", self.getDireccion(), "\nTelefono:", self.getTelefono(),"\nSaldo:", self.getSaldo())


if __name__ == "__main__":
	miCuentaCorriente=CuentaCorriente("Marcos","Monjon M","Cfemenias","61722222","3724712s")
	miCuentaCorriente.IngresarDinero(100)
	assert miCuentaCorriente.getSaldo() == 1100.0
	miCuentaCorriente.RetirarDinero(400)
	assert miCuentaCorriente.getSaldo()
	assert miCuentaCorriente.saldoNegativo() == False
	miCuentaCorriente.RetirarDinero(800)
	assert miCuentaCorriente.getSaldo() == -100.00
	assert miCuentaCorriente.saldoNegativo() == True
	assert miCuentaCorriente.getNombre() == "Marcos"
	assert miCuentaCorriente.getSaldo() == -100.0
	miCuentaCorriente.consultarCuenta()




