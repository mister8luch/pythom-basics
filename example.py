#crear lista
lista =[1,5,25,100,500]
print("inicial: ",lista)

#append()=agregar un dato final a la lista 
lista.append(250)
print("append :",lista)

# 
lista2=[75,125]
lista.extend(lista2)
print ("extend:" ,lista )

#
lista.insert(2,400)
print("insert: ",lista)
#elimina el dato entregado solo el primero que encuentre
lista.remove(400)
print("remove: ", lista)

#
lista.pop()
print("Pop:" ,lista)
lista.pop(2)
print("pop(2)",lista)
#
lista.reverse()
print("reverse:",lista)
#
#sort=ordenar de menor a mayor
lista.sort()
print("sort ", lista)

#sort()=ordenar de mayor a menor 
lista.sort(reverse=True)
print("sort(r):", lista)

#reverse 
lista=[3,2,1]
print(lista)
lista.reverse()
print(lista)