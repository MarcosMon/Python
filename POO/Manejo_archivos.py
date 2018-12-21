from io import open

# open sirve para abrir el archivo especificado con la sentencia que queramos, en este caso "w" write

archivo_texto=open("archivo.txt","w") 

#Creamos una variable con una frase
# Y la añadimos al documento con .write y la variable

frase="Estupendo dia para estudiar Python \n Hoy es jueves"

archivo_texto.write(frase)

archivo_texto.close()

#---------------------------------- Sirve para leer el archivo "r" = read

archivo_texto=open("archivo.txt","r")

texto=archivo_texto.read()

archivo_texto.close()

print(texto)

#-----------------------------------Sirve para que se convierta en una array "r"=read

archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()

archivo_texto.close()

print(lineas_texto[0])



#------------------------- Sirve para escribir otra linea "a" = append

archivo_texto=open("archivo.txt","a")

archivo_texto.write("\n siempre es una buena idea el estudiar python")

archivo_texto.close()

