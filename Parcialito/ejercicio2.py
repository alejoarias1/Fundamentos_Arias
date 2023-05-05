import os
import re
import glob

def extraer_mails():
    txt=glob.glob("*.txt")
    for archivo in txt:
        with open (archivo,"r") as miarch1:
            contenido=miarch1.read()
            mails=re.findall('\w+[.-]?\w*[@]+gmail.com',contenido)
            with open ("base_de_datos.txt","w") as miarch2:
                for i in mails:
                    miarch2.write(i + "\n")

extraer_mails()
