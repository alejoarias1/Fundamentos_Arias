#1
'''
class Titan:
    def __init__(self,salud=100):
        self.salud=salud

    def salud_actual(self):
        return self.salud
    
    def recibir_ataque(self,puntos_de_daño):
        self.salud -= 1.5 * puntos_de_daño
        if self.salud<=0:
            self.salud=0

    def destruir_casas(self,numero_de_casas):
        if numero_de_casas>self.salud*0.08:
            return False
        
    def esta_vivo(self):
        if self.salud>0:
            return True

titan1=Titan(100)
print(titan1.esta_vivo())
print(titan1.salud_actual())
'''

#2

class Enterprise:
    def __init__(self,potencia=50,coraza=5):
        self.potencia=potencia
        self.coraza=coraza

    def encontrarPilaAtomica(self):
        self.potencia += 25
        if self.potencia>=100:
            self.potencia=100
    
    def encontrarEscudo(self):
        self.coraza+=10
        if self.coraza>=20:
            self.coraza=20
    
    def recibirAtaque(self,puntos):
        self.coraza-=puntos
        if puntos>self.coraza:
            self.coraza=0
            self.potencia -= puntos-self.coraza
            if self.potencia<=0:
                self.potencia=0

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.potencia)
print(enterprise.coraza)