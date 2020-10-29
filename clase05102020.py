condicion = False
if condicion == True:
    print ("A condición cúmplese")
else:
    print ("A condición non se cumple")
    print("A condición non se cumple")
    print("A condición non se cumple")

numero = 0
if numero == 0:
    print("O número é cero")
elif numero == 1:
    print("O número é un ")
elif numero ==2:
    print("O número é dous")
else:
    print("A condición non se cumple")

# A if C else B

valor = "Par" if (numero % 2 == 0) else "Impar"

while numero < 15:
    numero = numero + 1
    print ( "Numero: " + str(numero))

numero = 0

while True:
    numero = numero + 1
    print ( "Numero: " + str(numero))
    if numero >= 15:
        print ("Rematamos o ciclo")
        break

serie = [ 1, 2, 3, 4]
for numero in serie:
    print (numero)
"""
int vector [] = { 1, 2, 3, 4}
for ( int i =0; i < 5; i++) {
    println ("%d\n", vector [i]);
    }
"""

def  nome_funcion (parametro1, parametro2):
    """Esta función vai a imprimir os parámetros
    pasados como argumentos"""
    print (parametro1)
    print (parametro2)

nome_funcion ( "Ola", 4)
nome_funcion (parametro2="6", parametro1="Adeus")
#nome_funcion ("Que tal")

def  funcion2 (parametro1, parametro2 = 8):
    """Esta función vai a imprimir os parámetros
    pasados como argumentos"""
    print (parametro1)
    print (parametro2)
funcion2 ("Outra función", 10)
funcion2 ("De novo outra función")

def funcion3 (numero1, numero2, *masNumeros):
    print (numero1)
    print (numero2)
    for parametro  in masNumeros:
        print (parametro)


funcion3 (2, 5, 8, 10)

funcion3 (2, 5, 8, 10,1 ,1,2,4,6)

#Alternativa o bucle for en java con range

for i in range (2, 20, 3):
    print ("valor: " + str(i))







