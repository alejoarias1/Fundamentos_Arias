'''''
#1
#En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes. Además instanciá a un Titan y ejecutá las siguientes líneas:

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

#2

#Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise puede:
#encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
#encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
#recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
#La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la Enterprise

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

#4
#Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

class MedioDeTransporte:
    def __init__(self,combustible):
        self.combustible=combustible
    
    def cargar_combustible(self,cantidad):
        self.combustible+=cantidad
    
    def entran(self,personas):
        if self.maximo<=personas:
            return True
        else:
            return False

class Auto(MedioDeTransporte):
    def __init__(self,combustible,maximo=5):
        super().__init__(combustible)
        self.maximo=maximo

    def recorrer(self,kms):
        self.combustible-=1/2*kms
    
class Moto(MedioDeTransporte):
    def __init__(self,combustible,maximo=2):
        super().__init__(combustible)
        self.maximo=maximo
     
    def recorrer(self,kms):
        self.combustible-=1/2*kms

auto=Auto(10)
auto.recorrer(5)
print(auto.combustible)

#Estudiantes y Personas

#Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si duermen o si comen, o la gastan al hacer ejercicio, sin embargo en particular los estudiantes también gastan energía al estudiar y se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:
#Decirnos cuánta energía tienen.
#Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos (si duermen 4 ganan la mitad de energía, es decir 50).
#Recuperar energía al comer, ganando de esta manera 10 puntos.
#Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
#Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.
#Además los estudiantes tienen el siguiente comportamiento:
#Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
#Si aprueban su estado de ánimo pasa a ser "Feliz".
#Definí las clases Persona y Estudiante con los atributos y métodos correspondientes y hacé que esta última herede de la primera. 
'''''

class Personas():
    def __init__(self,energia):
        self.energia=energia

    def cuanta_energia(self):
        print (self.energia)
    
    def comer(self):
        self.energia += 10
    
    def hacer_ejercicio(self,horas):
        self.energia-=horas*25
    
    def esta_feliz(self):
        return False

class Estudiantes(Personas):
    def __init__(self,energia):
        self.energia=energia
    
    def estudiar(self,horas):
        self.energia-=horas*20

    def aprobar(self):
        self.esta_feliz=True

estudiante = Estudiantes(100)
print (estudiante.esta_feliz)
print(estudiante.aprobar())
print (estudiante.esta_feliz)