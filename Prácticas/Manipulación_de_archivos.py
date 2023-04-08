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

#ejercicio 6
with open ("salida.txt", "w") as salida:
    with open ("a.txt","r") as mi_arch6:
        for i in mi_arch6:
            if i.endswith("\n"):
                i.replace("\n"," ")
                salida.write(i)

#ejercicio 7
