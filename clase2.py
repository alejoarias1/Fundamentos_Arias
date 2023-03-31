import os, sys

#sys.argv toma los argumentos que le pasabamos al script por terminal.
#[1] significa que siempre voy a tomar el primero
#es decir leo solo la primera palabra que escriben en la terminal
archivo= sys.argv[1]

def saludador(nombre):
    return "Hola " + nombre

print (saludador("alejo"))

#EJERCICIO EN CLASE
#Armar un script que lea un archivo.txt y me cree otro (nuevo_archivo.txt) 
#con los primeros 5 caracteres del archivo que elegimos

#Opcion1
with open("nuevo_archivo.txt", "r") as mi_arch:
    with open("nuevo_archivo.txt", "a") as nuevo:
        nuevo.write(mi_arch.readline(5))


#Opcion2
texto_leido= open("nuevo_archivo.txt", "r").read()
print(texto_leido[0:6])


#Opcion3
texto_leido= open("nuevo_archivo.txt", "r").read()
texto_para_escribir=texto_leido[0:6]
with open("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_para_escribir)

#Tarea para el miércoles 22/3