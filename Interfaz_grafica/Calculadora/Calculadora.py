from tkinter import * 


raiz=Tk()

raiz.title("Calculadora Hello Kitty")

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

reset_pantalla=False

resultado=0

fondo=PhotoImage(file="fondo.png")
fondo1=Label(miFrame,image=fondo).place(x=0,y=0)
num7=PhotoImage(file="7.png")
num8=PhotoImage(file="8.png")
num9=PhotoImage(file="9.png")
num4=PhotoImage(file="4.png")
num5=PhotoImage(file="5.png")
num6=PhotoImage(file="6.png")
el1=PhotoImage(file="el1.png")
num2=PhotoImage(file="2.png")
num3=PhotoImage(file="3.png")
num0=PhotoImage(file="0.png")
rest=PhotoImage(file="restar.png")
mult=PhotoImage(file="multiplicar.png")
summ=PhotoImage(file="sumar.png")
igual=PhotoImage(file="igual.png")
divv=PhotoImage(file="dividir.png")
coma=PhotoImage(file="coma.png")






#---------------------------------Pantalla--------------------------------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)

pantalla.grid(row=1, column=1, padx=15, pady=30, columnspan=4, ipady=20, ipadx=70)

pantalla.config(background="Pink", fg="green", justify="right")

#----------------Pulsaciones Teclado -------------------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)

#------------------ Funcion Suma ------------------

def suma(num):
	global operacion

	global resultado

	global reset_pantalla

	resultado+=int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)



#---------------funcion resta------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-int(num)

		else:

			resultado=int(resultado)-int(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=int(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True



#----------------funcion el_resultado----------------

def el_resultado():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+int(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0




#------------------------------Fila1-----------------------------------------------

boton7=Button(miFrame, image=num7, width=35,height=44, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1,padx=5, pady=10)
boton7.config(background="Pink")
boton8=Button(miFrame, image=num8, width=35,height=44, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton8.config(background="Pink")
boton9=Button(miFrame, image=num9, width=35,height=44, background="Pink", command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3, )
boton9.config(background="Pink")
botonDiv=Button(miFrame, image=divv, width=35,height=44,command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)

#------------------------------Fila2-----------------------------------------------

boton4=Button(miFrame, image=num4, width=35, height=44, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1,padx=5, pady=10)
boton4.config(background="Pink")
boton5=Button(miFrame, image=num5, width=35, height=44, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton5.config(background="Pink")
boton6=Button(miFrame, image=num6, width=35, height=44, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
boton6.config(background="Pink")
botonMult=Button(miFrame, image=mult, width=35, height=44, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

#------------------------------Fila3-----------------------------------------------

boton1=Button(miFrame, image=el1, width=35, height=44, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1, padx=5, pady=10)
boton1.config(background="Pink")
boton2=Button(miFrame, image=num2, width=35, height=44, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton2.config(background="Pink")
boton3=Button(miFrame, image=num3, width=35, height=44, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
boton3.config(background="Pink")
botonRest=Button(miFrame, image=rest, width=35, height=44, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

#------------------------------Fila4-----------------------------------------------

boton0=Button(miFrame, image=num0, width=35, height=44, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=1, padx=5, pady=10)
boton0.config(background="Pink")
botonComa=Button(miFrame, image=coma, width=35, height=44, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, image=igual, width=35, height=44, command=lambda:el_resultado())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, image=summ, width=35, height=44, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5, column=4)

raiz.mainloop()