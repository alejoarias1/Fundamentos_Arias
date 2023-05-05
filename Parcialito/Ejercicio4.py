class PacMan:
    def __init__(self,vidas=3,puntos=0):
        self.vidas=vidas
        self.puntos=puntos
    
    def comer_bolita(self,cantidad):
        self.puntos+=cantidad*2 #gana el doble de puntos que la cantidad q come
        
    def velocidad(self):
        return 2 + self.puntos / 100 #formula inventada
     
    def perderVida(self):
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER")

    def comerFantasma(self,fantasma):
        if fantasma == "rosa":
            self.puntos+=8
            self.velocidad+=1
    
        if fantasma == "verde":
            self.puntos+=6
            self.velocidad+=1
        
        if fantasma == "naranja":
            self.puntos+=4
            self.velocidad+=1
    
        if fantasma == "rojo":
            self.puntos+=2
            self.velocidad+=1

pacman=PacMan()
print(pacman.puntos)
pacman.comer_bolita(10)
print(pacman.puntos)
        
#version mejorada

class PacMan:
    def __init__(self,vidas=3,puntos=0):
        self.vidas=vidas
        self.puntos=puntos
    
    def comer_bolita(self,cantidad):
        self.puntos+=cantidad*2 #gana el doble de puntos que la cantidad q come
        
    def velocidad(self):
        return 2 + self.puntos / 100 #formula inventada
     
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print("GAME OVER")

    def comerFantasma(self,fantasma):
        if fantasma == "rosa":
            self.puntos+=8
            self.velocidad+=1

class Fantasma:
    def __init__(self):
        self.color=None

    def set_color(self,color):
        self.color = color

    def puntos_color(self):
        return self.color.puntos()

class Rojo:
    def puntos(self):
        return 2

class Naranja:
    def puntos(self):
        return 4

class Verde:
    def puntos(self):
        return 6

class Rosa:
    def puntos(self):
        return 8
    
#b
class PacManMejorado(PacMan):
    def vidaExtra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print ("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")
    def velocidad(self):
        return 3 + self.puntos / 100
   
   




    
    
    