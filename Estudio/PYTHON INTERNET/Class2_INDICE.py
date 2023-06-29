#INDICES
mystr = "hello world"
#Muestra todos los metodos para los indices
    #print(dir(mystr))
#Mayusc
print(mystr.upper())
#Minusc
print(mystr.lower())
#Alternado
print(mystr.swapcase())
#Inicia con Mayuscula la primera letra
print(mystr.capitalize())
#Remplaza la el caracter indicado 
print(mystr.replace("hello world","milaneso"))
#Hace una cuenta del caracter indicado
print(mystr.count(" "))
#Muestra si inicia con la palabra especificada
print(mystr.startswith("hello"))
#Muestra si termina con la palabra indicada
print(mystr.endswith("world"))
#Separa por el caracter indicado
print(mystr.split("o"))
#Muestra la posicion del caracter indicado
print(mystr.find("h"))
#Te muestra la longitud de la variable
print(len(mystr))
#Te muestra el indice de una palabra especificada
print(mystr.index("e"))
#Muestra si la variables es numerica
print(mystr.isalnum())
#Muestra si la variable es alfanumerica
print(mystr.isalpha())
#Muestra la el caracter que esta en la posicion indicada
print(mystr[4])

#Texto antes de mandar a llamar a la variable
print("My name is Diego, " + mystr)
#Se coloca la f antes del texto para indicar que el contenido dentro de la llave es un dato
print(f"My name is {mystr} ")
#Otra forma de hacerlo es usar .format
print("My name is {0}".format(mystr))