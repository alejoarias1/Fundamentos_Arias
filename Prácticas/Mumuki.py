#Para ello vamos a definir dos clases, Zombi y SuperZombi. De ellas sabemos que:

#ambas tienen un atributo hambre;
#ambos tipos de zombis saben correr;
#los super zombis son siempre un peligro, mientras que los zombis solo si tienen más de 50 de hambre;
#los zombis no saben regenerarse;
#los super zombis pasan a tener 100 de hambre al recibir el mensaje regenerarse;
#ambos tipos de zombis pueden recibir_danio con una cantidad de daño recibida como argumento. Al hacerlo, disminuye su hambre. En el caso de los super zombis disminuye la cantidad recibida y en el de los zombis el doble de esa cantidad.
#Definí las clases Zombi y SuperZombi.
#Definí los métodos sabe_correr, es_un_peligro, recibir_danio y regenerarse donde correspondan.
#Definí el constructor en cada una que permita dar un valor inicial al hambre.

class Zombi:
  def __init__(self,hambre):
    self.hambre=hambre
   
  def sabe_correr(self):
    return True
  
  def es_un_peligro(self):
    if self.hambre>50:
      return True
    else:
      return False
  
  def recibir_danio(self,daño):
    self.hambre -= daño*2
    
class SuperZombi:
  def __init__(self,hambre):
    self.hambre=hambre
   
  def sabe_correr(self):
    return True
  
  def es_un_peligro(self):
   return True
    
  def regenerarse(self):
    self.hambre=100
  
  def recibir_danio(self,daño):
    self.hambre -= daño


#Del equipo de cocina sabemos que:

#cada chef tiene un atributo plato_del_dia;
#las instancias de Chef pueden picantear ese plato solo si no está demasiado picante, en caso de estarlo arrojan una excepción que dice El plato ya está demasiado picante;
#las instancias de AyudanteDeCocina no tienen atributos ya que pueden suavizar cualquier plato que reciban como argumento.
#Mientras que de los platos podemos contar lo siguiente:

#las Pastas tienen un atributo ajies que inicialmente es 0;
#están demasiado picantes cuando tienen más de 10 ajies;
#al ser picanteadas aumenta en 5 su cantidad de ajies y al ser suavizadas pierden 1. No te preocupes por si al suavizar queda una cantidad negativa de ajies, no vamos a considerar ese escenario;
#las Pizzas tienen condimento que inicialmente es "adobo";
#se considera que una pizza está demasiado picante si su condimento es "cayena";
#al suavizar una pizza su condimento pasa a ser "orégano" y al picantearla, "cayena".
#Los constructores en ambos platos solo deben tener self como parámetro porque sus atributos siempre se inicializan con el mismo valor. 

class Chef:
  def _init_ (self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
  
  def picantear (self):
    if self.plato_del_dia.muy_picante():
      raise Exception ("El plato ya está demasiado picante")
    else:
      self.plato_del_dia.picante()

    
class AyudanteDeCocina:
  def suavizar (self, plato):
    plato.suavizar()
    
class Pizza:
  def _init_ (self):
    self.condimento = "adobo"

  def muy_picante (self):
    return self.condimento == "cayena"
    
  def suavizar(self):
    self.condimento = "orégano"
    
  
  def picante(self):
    self.condimento = "cayena"
    
class Pasta:
  def _init_ (self):
    self.ajies = 0
   
  def muy_picante (self):
    return self.ajies > 10
    
  def picante(self):
      self.ajies += 5
  
  def suavizar(self):
      self.ajies -= 1


#Por ahora nuestras opciones son limitadas. Podemos elegir ir en Auto o en Moto. De estos medios sabemos que:

#ambos comienzan con una cantidad que podemos establecer de combustible;
#los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido;
#las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
#ambos pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible;
#ambos saben responder si entran_personas a partir de una cantidad recibida como argumento. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

#Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera. 
# También definí los métodos __init__, recorrer, cargar_combustible, entran_personas y maximo_personas donde correspondan.

class MedioDeTransporte:
  def __init__(self,combustible):
    self.combustible=combustible
  
  def cargar_combustible(self,cantidad):
    self.combustible+=cantidad

  def entran_personas(self,cantidad):
    return cantidad<=self.maximo_personas()
    
class Moto(MedioDeTransporte):
  def recorrer(self,km):
    self.combustible-=km
  
  def maximo_personas(self):
    return 2
  
class Auto(MedioDeTransporte):
  def recorrer(self,km):
    self.combustible-=km/2
  
  def maximo_personas(self):
    return 5