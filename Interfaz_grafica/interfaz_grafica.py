from tkinter import *


raiz=Tk()

raiz.title("Formulario")

raiz.resizable(1,1)

#raiz.iconbitmap("nombre.imagen")

#raiz.geometry("400x200")

raiz.config(relief="groove")

raiz.config(bd=55)

raiz.config(cursor="hand2")

raiz.config(bg="grey")

miFrame=Frame()

miFrame.pack()

miFrame.config(bg="green")

miFrame.config(width="520", height="450")

miFrame.pack(side="bottom", anchor="e")

miFrame.pack(fill="x", expand="True") 

miFrame.config(relief="groove")   # el tipo de borde

miFrame.config(bd=35) # el borde es de 35 

miFrame.config(cursor="pirate") # el cursor del Frame es una calavera
"""
miImagen=PhotoImage(file="descarga.png") #declaramos la imagen en una variable

miLabel=Label(miFrame, image=miImagen) # al Frame le añadimos una imagen

misegundo=Label(miFrame, text="Bienvenidos a mi nueva interface", fg="blue",font=("Comic Sans",14)) # tamaño de letra, tipo, fuente y texto

misegundo.place(x=240, y=-10) # situar en este caso el texto a donde queremos

miLabel.place(x=600, y=-10) # situar en este caso la imagen a donde queremos
"""

minombre1=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre1)
cuadroNombre.grid(row=0, column=1, padx=10, pady=15)
cuadroNombre.config(fg="red", justify="center")
miNombre=Label(miFrame, text="User:")
miNombre.grid(row=0, column=0,padx=10, pady=10)

cuadroPW=Entry(miFrame)
cuadroPW.grid(row=1, column=1, padx=10, pady=15)
cuadroPW.config(fg="red", justify="center", show="*")
miPW=Label(miFrame, text="Password:")
miPW.grid(row=1, column=0, padx=10, pady=10)

cuadroDNI=Entry(miFrame)
cuadroDNI.grid(row=2, column=1, padx=10, pady=15)
miDNI=Label(miFrame, text="Apellidos:")
miDNI.grid(row=2, column=0, padx=10, pady=10)

textoComentario=Text(miFrame, width=20, height=10)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

miComentario=Label(miFrame, text="Comentarios:")
miComentario.grid(row=4, column=0, padx=10, pady=10)

scrollvert=Scrollbar(miFrame, command=textoComentario.yview)

scrollvert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollvert.set)

def codigoBoton():
	nombres=minombre1.get()

	print(nombres)


botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()


raiz.mainloop()   # es el bucle para que se ejecute todo



