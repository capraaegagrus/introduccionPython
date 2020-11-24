#from paquete.novoModulo import funcion as func
import paquete.novoModulo
from excepcions import Punto, Cilindro


def funcion ():
    print ("Función do main")



# clase = novoModulo.UnhaClase()

punto = Punto(2, 3)
c = Cilindro(3, 4, 5)

if __name__ == "__main__":
    funcion()
    paquete.novoModulo.funcion()
    #func()
