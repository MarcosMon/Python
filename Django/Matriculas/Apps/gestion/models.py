from django.db import models



class Alumno(models.Model):

	Apellido1= models.CharField(max_length=20)
	Apellido2= models.CharField(max_length=20)
	Nombres= models.CharField(max_length=20)
	DNI= models.CharField(max_length=9)
	FechaNacimiento= models.DateField()
	SEXOS= (("F","Femenino"),("M","Masculino"))
	sexo= models.CharField(max_length=1, choices=SEXOS, default="F")


	def NombreCompleto(self):

		cadena="{0} {1}, {2}"
		return cadena.format(self.Apellido1, self.Apellido2, self.Nombres)


	def __str__(self):

		return self.NombreCompleto()


class Curso(models.Model):

	Nombre=models.CharField(max_length=30)
	Creditos=models.PositiveSmallIntegerField()
	Estado=models.BooleanField(default=True)

	def __str__(self):

		return "{0} ({1})".format(self.Nombre,self.Creditos)

class Matricula(models.Model):

	Alumno=models.ForeignKey(Alumno, null=False, blank=False,on_delete=models.CASCADE)
	Curso=models.ForeignKey(Curso, null=False, blank=False,on_delete=models.CASCADE)
	FechaMatricula= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		cadena= "{0} => {1}"
		return cadena.format(self.Alumno, self.Curso.Nombre)



