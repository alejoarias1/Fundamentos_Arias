#ejercicio 1
def procedimiento (lista):
    for i in lista :
        if i == "control":
            posicion = lista.index(i)
            lista.insert(posicion,"revisado")
            lista.remove (i)
    print(lista)

lista = ["a", "control", "c"]
procedimiento (lista)

#ejercicio 2
def ejercicio2 (lista3):
    lista3.pop(0)
    print(lista3)

lista3=[1,2,3]
ejercicio2(lista3)

#ejercicio 3
def ejercicio3(elemento):
    lista2=["e","y","a"]
    for i in lista2:
        return lista2.index(elemento)
    
print(ejercicio3("a"))

#ejercicio 4
def ejercicio4(lista4,lista5,elemento):
    for i in lista4:
        if i==elemento:
            lista4.remove(i)
            lista5.append(i)
    print(lista4)
    print(lista5)

lista4=[1,2,3]
lista5=[4,5,6]
ejercicio4(lista4,lista5,1)

#ejercicio5
def ejercicio5(lista6):
    par_impar=[]
    for i in lista6:
        if i %2==0:
            par_impar.append(True)
        else:
            par_impar.append(False)
    return par_impar
            
lista6=[1,2,3,4]
print(ejercicio5(lista6))


