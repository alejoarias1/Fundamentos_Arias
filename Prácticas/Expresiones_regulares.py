import re

#ejercicio 1
texto="Escribí un programa que verifique si un string tiene al menos un carácter permitido"
a=re.findall(r'[a-zA-Z0-9]',texto)
if len(a)>0:
    print ("el string tiene al menos un caracter permitido")
else:
    print ("el string no tiene ningun caracter permitido")

#ejercicio 2
texto="Escribí un programa que verifique si un string tiene al menos un carácter permitido"
b=re.findall(r'[a-zA-Z0-9]',texto)
if len(b)>67:
    print ("el string tiene todos los caracteres permitidos")
else:
    print ("el string no tiene todos los caracteres permitidos")

#ejercicio 3
texto="Escribí un programa que verifique si un string tiene al menos un carácter permitido"
he=re.findall(r'he*',texto)
if len(he)>0:
    print("el string dado tiene una h seguida de ninguna o más e.")
else:
    print ("el string dado no tiene una h seguida de ninguna o más e.")

#ejercicio 5
string= "1 hombre fue a la playa"
c=re.search(r'1', string)
if c!=None:
    print("el string comienza con 1")
else:
    print("el string no comienza con 1")

#ejercicio 7
frase="soy de racing el mas grande del pais"
lista_strings=["boca","mas","grande"]
for i in lista_strings:
    if i in frase:
        print("la palabra "+ i +" se encuentra en la frase")
    else:
       print("la palabra "+ i +" no se encuentra en la frase")

#ejercicio 8
numeros="1,4,5,6,4"
buscador_numeros=re.findall(r'\d',numeros)
print(buscador_numeros)

#ejercicio9
string2= "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(re.findall(r'-.+-',string2))

#ejercicio12
stringg="Hoy estuvimos trabajando con re _regular expression_ en python: con VSCode-"
nuevo_string= re.sub(r"[ _:-]", "|", stringg)
print (nuevo_string)

#ejercicio 13
texto13="a 2 ! d ? jj"
texto13_mod=re.sub(r'\W{2}',"_", texto13)
print(texto13_mod)

#ejercicio 14
texto13_mod2=re.sub(r'[\s\t]',";",texto13)
print(texto13_mod2)