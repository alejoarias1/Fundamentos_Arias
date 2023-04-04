#!/bin/python3
import os, glob, sys

arch=open("hola.txt","r")
print (arch.read())
print (arch.readlines())

#PRÁCTICA

def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt")
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt: 
        #esto seria un "for i in txt"
        with open(archivo,"r") as file:
            file_completa = file.read()
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_estado.append(file_completa.count("\n")) #para ver saltos de lineas (?
    
    os.mkdir("Apellido") #si no nos aclara donde hay que crearla, la creamos donde estamos parados
    with open("Apellido/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo,"r") as file:
                primera_linea = file.readline()
                salida.write(primera_linea)

#no se puede probar porque no tenemos la carpeta Informes
#con los txt, pero asi seria el script