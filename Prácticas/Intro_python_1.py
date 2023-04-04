def ejercicio1 (a):
    print (a+1)
    print (a-1)

ejercicio1 (4)

def ejercicio2 (b):
    print (b*2)

ejercicio2(4)

def ejercicio3 (c):
    print ((c+1)*2)
    print ((c-1)*2)

ejercicio3(2)

#ejercicio 4
def retirar_dinero(saldo,monto_a_retirar):
    print(saldo - monto_a_retirar)
    if (saldo - monto_a_retirar)<0:
        print (0)
retirar_dinero(50,70) 
#REVISAR, ES SIN IF

#ejercicio5
def dia_de_la_semana_favorito(dia="Sábado"):
    return bool
dia_de_la_semana_favorito("Sábado")
#REVISAR, NO ME SALE

#ejercicio10
def saludador(nombre):
    return "Hola" + nombre

print (saludador("Alejo Arias"))

#ejercicio11
def ejercicio11(palabra):
    if palabra[0]=="H":
        print (len(palabra))
    else:
        print(palabra)
                  
ejercicio11("Ayer")