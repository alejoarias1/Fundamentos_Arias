import re

#ejercicio 1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
texto="Escribí un programa que verifique si un string tiene al menos un carácter permitido"
a=re.findall(r'[a-zA-Z0-9]',texto)
if len(a)>0:
    print ("el string tiene al menos un caracter permitido")
else:
    print ("el string no tiene ningun caracter permitido")

#ejercicio 2
#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
texto="Escribí un programa que verifique si un string tiene al menos un carácter permitido"
b=re.findall(r'[a-zA-Z0-9]',texto)
if len(b)>67:
    print ("el string tiene todos los caracteres permitidos")
else:
    print ("el string no tiene todos los caracteres permitidos")

#ejercicio 3
#Verifique 
#si un string dado tiene una h seguida de ninguna o más e.
texto="Escribí un programa que verifique si un string_tiene al menos un carácter permitido"
he=re.findall(r'he*',texto)
if len(he)>0:
    print("el string dado tiene una h seguida de ninguna o más e.")
else:
    print ("el string dado no tiene una h seguida de ninguna o más e.")

#ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
print(re.findall(r'\w+_\w+',texto))

#ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.
string= "1 hombre fue a la playa"
c=re.search(r'1', string)
if c!=None:
    print("el string comienza con 1")
else:
    print("el string no comienza con 1")

#ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
frase="soy de racing el mas grande del pais"
lista_strings=["boca","mas","grande"]
for i in lista_strings:
    if i in frase:
        print("la palabra "+ i +" se encuentra en la frase")
    else:
       print("la palabra "+ i +" no se encuentra en la frase")

#ejercicio 7


#ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
numeros="1,4,5,6,4"
buscador_numeros=re.findall(r'\d',numeros)
print(buscador_numeros)

#ejercicio9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
string2= "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
print(re.findall(r'-.+-',string2))

#ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
stringgg="Hoy fui al cine @Av. Corrientes& y vi una buena película @Los Vengadores&"
print(re.findall(r'@.+&',stringgg))

#ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

#ejercicio12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
stringg="Hoy estuvimos trabajando con re _regular expression_ en python: con VSCode-"
nuevo_string= re.sub(r"[ _:-]", "|", stringg)
print (nuevo_string)

#ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
texto13="a 2 ! d ? jj"
texto13_mod=re.sub(r'\W{2}',"_", texto13)
print(texto13_mod)

#ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
texto13_mod2=re.sub(r'[\s\t]',";",texto13)
print(texto13_mod2)

#ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.
def mail_correcto(string):
    return bool (re.search('^\w+[.-]?\w*[@][a-z]+[.][a-z]+[.]?[a-z]?$',string))
print(mail_correcto("alearias519@gmail.com"))

#ejercicio VV
#Buscar en la siguiente secuencia, todos los patrone que comiencen por & y caben por %$

def VV(string):
    print(re.findall(r'\&(.*?)\%\$',string))

VV("vwrevwn35n32o5n32n532jin532&vewkvnemvoseomom&l;mewvemwovew;m*&^6vaevvkems;vevm%$vewwv%$ feveve vkwe[31532095llc;ac7777&&&&&f32f45123%$")

# obtener la lista de los substrings delimitados entre '<' y '>' 
#que no incluyan ninguna 'o'.

def ejercicio(string):
    print(re.findall(r'<([^o]*?)>',string))

ejercicio("ds<hola>hsb<hhj>sdk<469>nkd")














