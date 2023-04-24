class Pacman:
    def __init__(self,velocidad=1,vidas=3,puntos=0):
        self.vidas=vidas
        self.puntos=puntos
        self.velocidad=velocidad
    
    def comer_bolita(self,cantidad):
        self.puntos+=cantidad
        return self.puntos
        return self.veolcidad
    
class Fantasma:
    def fantasma_rosa(self):
        self.puntos+=8
        self.velocidad+=1
        return self.puntos
        return self.veolcidad
    
    def fantasma_verde(self):
        self.puntos+=6
        self.velocidad+=1
        return self.puntos
        return self.veolcidad
    
    def fantasma_naranja(self):
        self.puntos+=4
        self.velocidad+=1
        return self.puntos
        return self.veolcidad
    
    def fantasma_rojo(self):
        self.puntos+=2
        self.velocidad+=1
        return self.puntos
        return self.veolcidad
    
   
   
   




    
    
    