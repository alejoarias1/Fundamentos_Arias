import os

#ejercicio 1
contador=0
with open ("a.txt","r") as mi_arch:
    a=mi_arch.readline()
    if a.startswith("P"):
        contador+=1
print(contador)

#ejercicio 2
with open ("a.txt","r") as mi_arch2:
    for i in range(1):
        print(mi_arch2.readlines())

#ejercicio 6
with open ("salida.txt", "w") as salida:
    with open ("a.txt","r") as mi_arch6:
        for i in mi_arch6:
            if i.endswith("\n"):
                i.replace("\n"," ")
                salida.write(i)
