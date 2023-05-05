import re

#1a
#como nos pide una lista, ya sabemos que hay que usar findall
def ejercicio1(string):
    return re.findall(r'[^X]*[a-b][^Y]*', string)

print(ejercicio1("XbaaaYjXababYqXbabbbaaYqXffee"))

#otra manera
def entre_X_Y_con_ab(string):
    return re.findall("X(.*?ab.*?)Y",string)

print(entre_X_Y_con_ab("XbaaaYjXababYqXbabbbaaYqXffee"))

#1b
#1. Falso, debe estar en minúscula y cada palabra separada por un guión bajo (snake_case). La funcion tambien deberia tomar un parametro.
#2. El error es AttributeError, ya que el findall esta mal escrito
#3. Verdadero, esta mal escrito, es findall no findal
#4. Verdadero
#5. Falso

#funcion modificada

def entre_ag_cta_sin_numeros(string):
    return re.findall("ag([^\d]*)cta",string)

print (entre_ag_cta_sin_numeros("aabocaggaaactazu4lggaasag24gra1ndecta"))