#Teoria:
#Variables y Constantes
name = "Fazt"  
#case sensitive
book = "digital fortres"    
Book = "digital fortres"  
#agrupacion en variable 
x, Num_Book = 100,"Persona normal"
#convenciones
    #book_name = "Yo robot" (Snake Case)
    #bookName = "Persona Normal" (Camel case)
    #BookName = "hola" (Pascal case)
book = "Neva Asignacion de variable"
#CONSTANTES
PI = 3.1416
    #Tipos de datos
        #(string:cadena de caracteres "")
        #(Integer (10))
        #(Float (20.23))  
        #(Boolean (true, false))
        #(List (10,20,"hello",true))
        #(Tuples (Datos definidos que no cambian), se define con parentesis) 
        #(Dictionarios, agrupacion de datos que estan definidos por clave y valor 
            #   {
            #   "name":"Ryan",
            #   "lastname""Ray",
            #   "nickname""Fazt",
            #   })
        #(None)  
        
#Mandar a imprimir 
print("hola mundo")
print(10 + 5.5)
#Se usa Type para especificar que tipo de dato es
print(type("hola mundo"))
print(type({
          "name":"Ryan",
          "lastname":"Ray",
          "nickname":"Fazt",
        }) )
#Unir strings:
print( "Hola" + ", MUNDO cruel")
#imprimir variable
print(name)
#imprimir valores agrupados en variables
print(x, Num_Book)
