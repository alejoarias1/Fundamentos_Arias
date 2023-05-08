import os
import glob
import re

#ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
contador=0
with open ("a.txt","r") as mi_arch:
    for line in mi_arch:
        if line.startswith("P"):
            contador+=1
print(contador)

#ejercicio 2
#Escribí un programa que lea un archivo e imprima las primeras n líneas.
with open ("a.txt","r") as mi_arch2:
    for i in range(1):
        print(mi_arch2.readlines())

#ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
def read_n_back_lines(n,archivo):
    texto=open(archivo,"r").readlines()
    for i in range ((len(texto) -n), len(texto)):
        print(texto[i])

#ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.
def contar_palabras(archivo):
    contador = 0
    with open(archivo, 'r') as mi_arch:
        for linea in mi_arch:
            palabras = linea.split()
            contador += len(palabras)
    print(contador)

#ejercicio 5
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.
def ejercicio5(letra):
    with open("a.txt", 'r') as miarch:
        for linea in miarch:
            nuevo_archivo=linea.replace(letra, letra + "\n")
        with open("a2.txt","w") as miarch2:
            miarch2.write(nuevo_archivo)

#ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.
with open ("salida.txt", "w") as salida:
    with open ("a.txt","r") as mi_arch6:
        for i in mi_arch6:
            if i.endswith("\n"):
                i.replace("\n"," ")
                salida.write(i)

#ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.
with open('a.txt', 'r') as mi_Arch:
    palabra_mas_larga = max(mi_Arch.read().split(), key=len)
    print("La palabra mas larga es", palabra_mas_larga)

#ejercicio 8
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

archivo1 = open("a.txt", "r")
archivo2 = open("a2.txt", "r")
archivo_nuevo = open("archivo_nuevo.txt", "w")

contenido1 = archivo1.read()
contenido2 = archivo2.read()

archivo_nuevo.write(contenido1)
archivo_nuevo.write(contenido2)

#Escribí un programa que abra dos documentos 
# y guarde la tercera linea de ambos en un otro documento llamado archivofinal

# Abrir los dos archivos de entrada
archivo1 = open("archivo1.txt", "r")
archivo2 = open("archivo2.txt", "r")

# Leer el contenido de cada archivo
lineas1 = archivo1.readlines()
lineas2 = archivo2.readlines()

# Extraer la tercera línea de cada archivo
linea3_archivo1 = lineas1[2]
linea3_archivo2 = lineas2[2]

# Crear un nuevo archivo llamado "archivofinal"
archivofinal = open("archivofinal.txt", "w")

# Escribir las líneas extraídas de los dos archivos en el nuevo archivo
archivofinal.write(linea3_archivo1)
archivofinal.write(linea3_archivo2)

# Cerrar todos los archivos
archivo1.close()
archivo2.close()
archivofinal.close()

#ejercicio 10
#Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un 
# archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.

def ejercicio10():
    os.chdir("Carpeta1")
    archivostxt=glob.glob("*.txt")
    if not os.path.exists("Resultados"):
        os.mkdir("Resultados")
    for archivo in archivostxt:
        with open (archivo, "r") as cada_archivo:
            txt=cada_archivo.readlines()
            print(txt) 
            os.chdir("Resultados")
            with open ("arbolito.txt","a") as salida:
                for lineas in txt:
                    salida.write(lineas + "\n")
            os.chdir("..")

print (ejercicio10())

#ejercicio extra
#lo mismo que el anterior pero te tiene que capturar los mails de los txt,
#no los txts enteros

def ejercicio_extra():
    os.chdir("Carpeta1")
    archivostxt=glob.glob("*.txt")
    if not os.path.exists("Resultados"):
        os.mkdir("Resultados")
    for archivo in archivostxt:
        with open (archivo, "r") as cada_archivo: 
            archivoss=cada_archivo.read()
            mails=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',archivoss)
            print (mails)
            os.chdir("Resultados")
            with open ("arbolito.txt","a") as salida:
                for lineas in mails:
                    salida.write(lineas + "\n")
            os.chdir("..")

print (ejercicio_extra())

#Deberás extraer los números de teléfono de CABA (+54911########) y guardarlos en un
#archivo nuevo, en una carpeta llamada” Telefonos”, creada dentro de la CarpetaParcial.

def extraer_numeros():
    os.chdir("CarpetaParcial")
    if not os.path.exists("Telefonos"):
        os.mkdir("Telefonos")
    telefonos=glob.glob("*.txt")
    for cada_telefono in telefonos:
        with open(cada_telefono,"r") as telefonoss:
            telefonostelefonos=telefonoss.read()
            telefonos_final=re.findall(r'\+54911[0-9]{8}',telefonostelefonos)
            print(telefonos_final)
            os.chdir("Telefonos")
            with open("lista_telefonos","a") as archivo_telefonos:
                for telefonos_xd in telefonos_final:
                    archivo_telefonos.write(telefonos_xd + "\n")
            os.chdir("..")

print(extraer_numeros())

#NO TE PODES MOVER PARA UNA CARPETA EN LOS COSTADOS, SOLO PARA ATRAS O ADELANTE