#ejercicio 1
#Escribir funciones que permitan obtener el anterior y el siguiente de un número.
def ejercicio1 (a):
    print (a+1)
    print (a-1)

ejercicio1 (4)

#ejercicio 2
#Escribir una función que obtenga el doble de un número.
def ejercicio2 (b):
    print (b*2)

ejercicio2(4)

#ejercicio 3
#Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.
def ejercicio3 (c):
    print ((c+1)*2)
    print ((c-1)*2)

ejercicio3(2)

#ejercicio 4
#Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y el monto a retirar y que devuelva cuánto saldo queda luego de la extracción. Si retira más dinero que lo que tiene en el saldo debe devolver 0 (no se puede usar if).
def retirar_dinero(saldo,monto_a_retirar):
    print(saldo - monto_a_retirar)
    if (saldo - monto_a_retirar)<0:
        print (0)
retirar_dinero(50,70) 
#REVISAR, ES SIN IF

#ejercicio5
#Escribir una función llamada dia_de_la_semana_favorito que tome como parámetro un día de la semana y devuelve True si el día es "Sábado" o False si es cualquier otro (no se puede usar if).
def dia_de_la_semana_favorito(dia="Sábado"):
    return bool
dia_de_la_semana_favorito("Sábado")
#REVISAR, NO ME SALE

#ejercicio10
#Escribir una función que reciba un nombre y un apellido y devuelva un saludo de bienvenida para esa persona.
def saludador(nombre):
    return "Hola" + nombre

print (saludador("Alejo Arias"))

#ejercicio11
#Escribir una función que tome como parámetro un string y que, si empieza con la letra "H", nos devuelva la longitud del string.
def ejercicio11(palabra):
    if palabra[0]=="H":
        print (len(palabra))
    else:
        print(palabra)
                  
ejercicio11("Ayer")