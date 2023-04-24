#ejercicio 1
#Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".
def procedimiento (lista):
    for i in lista :
        if i == "control":
            posicion = lista.index(i)
            lista[posicion]="revisado"
    print(lista)

lista = ["a", "control", "v"]
procedimiento (lista)

#ejercicio 2
#Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.
def ejercicio2 (lista3):
    lista3.pop(0)
    print(lista3)

lista3=[1,2,3]
ejercicio2(lista3)

#ejercicio 3
#Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.
def ejercicio3(elemento):
    lista2=["e","y","a"]
    for i in lista2:
        if i == elemento:
            return lista2.index(elemento)
    
print(ejercicio3("a"))

#ejercicio 4
#Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. Realizar dos versiones del ejercicio, usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?
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
#Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.
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

#ejercicio9
#Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.
def productoria(lista_numeros):
    product=1
    for i in lista_numeros:
        product*=i
    return product
productoria([1,2,3,4])        

