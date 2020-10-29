#Estruturas de datos en Python: tuplas, listas e diccionarios
lista = [2, 2.3, 5+3j, ["Pepe", "36123456F"],5,18,["Africa", "Asia", "Oceania"],15]
lista2 = list ()
print (lista [2])
print (lista [-2])
print (lista [3][1])
for valor in lista:
    print (valor)

#slicing (inicio:fin:salto)
print (lista [2:7])
print (lista [2:])
print (lista [:5])
print (lista [1:6:2])
print (lista [1::2])
#lista [3] = "Outro valor"
print (lista)
lista [1:5] = ["Outros", "valores", "sustitutos"]
print (lista)

#Tuplas
tupla = (2, 2.3, 5+3j, ["Pepe", "36123456F"],5,18,("Africa", "Asia", "Oceania"),15)
print (type (tupla))
tupla2 = "Africa", "Asia", "Oceania"
#tupla2 [1] ="Australia"
print (tupla2[1])
tupla3 = (3,)
tupla4 = 4,
tupla5 = (5)
print (type (tupla3), type (tupla5))
tupla [3][1] = "Non ten dni"
#listaTupla = tupla [3]
#print (type (listaTupla) )
#listaTupla [1] = "Non ten dni"
print (tupla)
dicionario = { "un": 1,
               "dous": 2,
               "tres": 3,
               1: "un"}
print (dicionario ["un"])
print (dicionario [1])

lista.append ("novo valor engadido con append")
lista.extend (["outro", "outro", ("outro",)])
lista.insert (4, "inserto")
print (lista)
print (lista.count (['Africa', 'Asia', 'Oceania']))
print (lista.count (('outro',)))
print (len(lista))
print (lista.index ('outro',10, 12))
lista.pop (4)
lista.remove( 'outro')
lista.reverse()
lista2 =[3,2,5,7,5,9,3]
lista2.sort()
print (lista2)
lista3 = [("Ana", 15),("Raúl", 17), ("Belen", 16)]

def comparacion (elemento):
    return elemento[1]

lista3.sort(key= comparacion, reverse=True)
print (lista3)





