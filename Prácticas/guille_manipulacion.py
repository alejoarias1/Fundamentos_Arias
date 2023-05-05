import os
import glob

#Definir un procedimiento que lea los archivos .txt que estan en la crpeta marzo, 
#copie la primera linea cada uno en un archivo dentro de la carpeta resultados 
#(que debe estar dentro de new)

#pasos:
#movemos a marzo
#extraemos los .txt
#leemos las primeras lineas
# hacemos carpeta de salida (resultados)
#hacer archivo nuevo
#poner lineas en archivo nuevo


def primeras_lineas(path_txt,path_resultado,salida):
    os.chdir(path_txt) #se mueve a carpeta marzo
    archivos_txt=glob.glob("*.txt") #agrupa los txt de marzo
    primer_linea=[]
    for txt in archivos_txt:
        with open (txt,"r") as textos:
            primer_linea.append(textos.readline())
    os.chdir("../../") #volvemos a la carpeta new
    os.mkdir(path_resultado) #creamos carpeta rtdos (path_rtdos es el nombre)
    os.chdir(path_resultado) #nos movemos a carpeta creada
    with open (salida , "a") as final_txt:
        for i in primer_linea:
            final_txt.write(i)

