demo_list = [1, "Hello", 1.34, True, [1,2,3]]
colors = ["red", "green", "blue","red"]

numbers_list  = list((1,2,3,4))
#print(type(numbers_list))

#crear una lista apartir del rango = list(range(1,100))
#dir para mostrar los metodos de la lista
#print(colors[-2])
#muestra si pertenece a la variable colors print("green" in colors)

#Sirve para alterar los datos de una lista
# print(colors)
# colors[1]="yellow"
# print(colors)
#print(dir(colors))
#print(len(colors))

#Se usa append para agregar un nuevo elemento
#colors.append("violet, yellow")
#print(colors)
#colors.extend(["violet", "yellow"])
#colors.extend(["black", "pink"])
#colors.insert(-1, "Violet")
#colors.insert(len(colors), "Violet")
#print(colors)
#Quitar elementos usando .pop
#colors.pop()
#print(colors)

#Remover un elemento por su nombre
#colors.remove("green")
#print(colors)

#Remover toda la lista
#colors.clear()

#Ordenar 
#colors.sort(reverse=True)

#Obtener indice
#print(colors.index("green"))

#Cuenta cuantos mismos elementos hay
print(colors.count("red"))
