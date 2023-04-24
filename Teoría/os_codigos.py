import os

print(os.getcwd()) #Para mostrar donde estoy ubicado

print(os.listdir()) #Para listar los archivos de mi actual ubicacion

lista = os.listdir() #Guardart los archivos de un directorio dentro de una lista

os.chdir("path del directorio al que me quiero mover")

os.mkdir("nombre de la carpeta a crear")

os.remove("carpeta a borrar")

os.rename("nombre antiguo, nombre nuevo")