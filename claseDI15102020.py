def nome_funcion ( parametro1, parametro2, parametro3 = "estás"):
    print (parametro1)
    print (parametro2)
    print (parametro3)


nome_funcion ( parametro2 ="Ola" , parametro1= "que tal", parametro3 = "Manuel")


def funcion2 ( parametro1, parametro2, parametro3 = "estás", *outros):
    print (parametro1)
    print (parametro2)
    print (parametro3)
    for variable in outros:
        print (variable)

funcion2 ("Ola", "que tal")
funcion2 ("Ola", "que tal", "Manuel")
funcion2 ("Ola", "que tal", "Manuel",1, 2, 3,4,5,6,"..." )


def funcion3 ( parametro1, parametro2, parametro3 = "estás", **outros):
    print (parametro1)
    print (parametro2)
    print (parametro3)
    #print (outros.keys())
    #print (outros.values())
    for clave in outros.keys():
        print (clave, " = '", outros [clave], "'")
    for valor in outros.values():
        print (valor)

funcion3 (parametro1 = "Ola", parametro2 = "de novo", parametro3 = "imos ver", parametro4 = "as funcións", parametro5 = "con número", parametro6= "variable de", parametro7 = "parámetros")

def produto ():
    #Exercicio 1.5.2
    print ("Cálculo do produto de dous números ")
    n1 = input ("Introduce o primeiro número: ")
    n2 = input ("Introduce o segundo número: ")
    print ( "O produto é: ", int(n1)*int(n2))

produto()

def suma2 (n1, n2, *restoValores):
    suma = n1 + n2
    for valor in restoValores:
        suma = suma + valor
    print (suma)

suma2 (5, 4)
suma2 (5,4,12,6,8,6, 22.5)

#Exercicio 1.8.1
def calculos (n1, n2):
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion =  n1 * n2
    division = n1 / n2
    return suma, resta, multiplicacion, division

var = calculos (8, 2)
sum, rest, mult, div = calculos (10, 5)
print (sum)

def esta_a_tupla_ordeada(tupla):
    ordeada = True
    valor1 = tupla [0]
    for valor in tupla:
        if valor1 > valor :
            ordeada = False
        valor1 = valor
    return ordeada

print (esta_a_tupla_ordeada ((3,9,6,7,7,9)))
