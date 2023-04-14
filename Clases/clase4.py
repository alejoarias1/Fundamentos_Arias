import re
import re
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto)) #busca en todo el texto, la primera aparición
print(re.match(patron,texto)) #busca solo al principio del texto
print(texto[22:26])
print(re.findall(patron,texto)) #te va a traer todas las apariciones
print(re.search(patron, texto).group()) #me junta todos los caracteres 
#que fueron resultado de mi búsqueda
