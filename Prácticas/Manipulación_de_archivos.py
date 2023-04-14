import os

#ejercicio 1
contador=0
with open ("a.txt","r") as mi_arch:
    for line in mi_arch:
        if line.startswith("P"):
            contador+=1
print(contador)

#ejercicio 2
with open ("a.txt","r") as mi_arch2:
    for i in range(1):
        print(mi_arch2.readlines())

#ejercicio 3
def read_n_back_lines(n,archivo):
    texto=open(archivo,"r").readlines()
    for i in range ((len(texto) -n), len(texto)):
        print(texto[i])

#ejercicio 4
def contar_palabras(archivo):
    contador = 0
    with open(archivo, 'r') as mi_arch:
        for linea in mi_arch:
            palabras = linea.split()
            contador += len(palabras)
    print(contador)

#ejercicio 6
with open ("salida.txt", "w") as salida:
    with open ("a.txt","r") as mi_arch6:
        for i in mi_arch6:
            if i.endswith("\n"):
                i.replace("\n"," ")
                salida.write(i)

#ejercicio 7
with open('a.txt', 'r') as mi_Arch:
    palabra_mas_larga = max(mi_Arch.read().split(), key=len)
    print("La palabra mas larga es", palabra_mas_larga)

#ejercicio 8

archivo1 = open("a.txt", "r")
archivo2 = open("a2.txt", "r")
archivo_nuevo = open("archivo_nuevo.txt", "w")

contenido1 = archivo1.read()
contenido2 = archivo2.read()

archivo_nuevo.write(contenido1)
archivo_nuevo.write(contenido2)