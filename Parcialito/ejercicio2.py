import os
import re

def extraer_mails():
    with open ("mails.txt","r") as miarch1:
        contenido=miarch1.read()
        mails=re.findall('\w+[.-]?\w*[@][a-z]+[.][a-z]+[.]?[a-z]?$',contenido)
        with open ("base_de_datos.txt","w") as miarch2:
            for i in mails:
                miarch2.write(i)

extraer_mails()
