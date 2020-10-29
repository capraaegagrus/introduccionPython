import math

class Punto:
    """Clase que define un punto"""

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y



meuPunto = Punto (4,5)
meuPunto.x = 10
print (meuPunto.x)

class Circulo (Punto):
    def __init__ (self, x = 0, y = 0, r=1):
        Punto.__init__(self, x, y)
        self.r = r

    def superficie (self):
        return math.pi*self.r**2

    def perimetro (self):
        return 2*math.pi*self.r


class Altura :
    def __init__ (self, h = 1):
        self.__h = h

    def getH(self):
        return self.__h


class Cilindro (Circulo, Altura):
    def __init__ (self, x=0, y=0, r=1, h=1):
        Circulo.__init__ (self, x, y, r)
        Altura.__init__ (self, h)

    def volume (self):
        return Circulo.superficie(self)*self.getH()

    def superficie (self):
        return Circulo.superficie(self)*2+ self.getH()*self.perimetro()

    def __privado (self):
        print ("Método privado")

    def publico (self):
        self.__privado()


c = Cilindro ()
print (c.volume())
print (c.superficie())
print (c.x)
print (c.getH())
c.publico()
c.__privado()










