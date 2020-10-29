lista = [1, 3,5, 6, "Cadeas", 2.3, True, ["outra lista", 2, 5]]
print (lista [5])
print (lista [7][1])
print (lista  [-1][1])

print (lista [0:3])
print (lista [:3])
print (lista [1:7:2])
print (lista [::2])
lista [3] = False
print (lista)
lista [0:2] = [7,8,9,0.10]
print (lista)
lista2 = list()
#lista2 = []
print (type (lista2))

tupla = (1,3, "Hola", True, (4, "Que tal"))
tupla2 = 1,

print (type (tupla2))

diccionario = {
    "Azul" : "#2E86C1",
    "Vermello" : "#E74C3C",
    "Verde" : "#2ECC71"
}

print (diccionario ["Verde"])

print (diccionario.get ("Verdessss", "O obxecto non existe"))
print ("Verde" in diccionario)
print (diccionario.items())



for entrada in diccionario.items():
    print ("Clave: " + entrada[0] + "\t\t Valor: " + entrada[1])


print ('Borrando a entrada con clave: "Verde"\nQue devolta o valor: ' + diccionario.pop ("Verde", "#000000") )
print (diccionario.keys())
print (diccionario.values())

#Ampliación de cadeas

cadea ="Unha cadea para traballar como exemplo de cadeas"
print (cadea.count ("cadea"))
print (cadea.find ("cadea",6, 30))
print (cadea.join(("Ola", "que", "tal", "estas")))
print (cadea.partition (' '))
print (cadea.split (' ', 5))
print (cadea.replace ('cadea', "*****", 1))



