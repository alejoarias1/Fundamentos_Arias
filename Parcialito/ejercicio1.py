import re

#1a
def ejercicio1(string):
    print(re.findall(r'X[ab][ab]+Y', string))

ejercicio1("XabYjXabababY")

#1b
#1. Falso, debe estar en minúscula y cada palabra separada por un guión bajo (snake_case)
#2. Falso, lanza SyntaxError
#3. Verdadero, esta mal escrito, es findall no findal
#4. Verdadero
#5. Falso