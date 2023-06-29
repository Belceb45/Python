#Comparacion son if 

#Funcion con numeros
# x=input("Inserta un numero: ")
# if int(x) < 20:
#     print("x es menor 20")
# else:
#     print("x es mayor a 20")

# #Funcion con strings
# color=input("Escribe un color: ")
# if str(color)=="red":
#     print("El color coincide")
# else:
#     print("El color no coincide")

# #Elif
# Edad=input("Inserta tu edad: ")
# if int(Edad)>20:
#     print("Puede pasar")
# elif int(Edad) == 18:
#     print("Muestrame tu identificacion")
# else:
#     print("No puede pasar")
    

#If dentro de un If
  
# name=input("Ingrese su nombre: ")
# last_name=input("Ingrese su apellido: ")
# if name == "Jhon":
#     if last_name=="Carter":
#         print("Puede ingresar")
#     else:
#         print("No puede ingresar")
# else:
#     print("No puede ingresar")

#Operdadores logicos
x=input("Ingrese un numero: ")

y=input("Ingresa un numero:")

if int(x) >2 and x <=10:
    print("x es mas grande que 2 pero menor o igual a 10")

if int(x) >2 or x <=20:
    print("x es mayor a 2 o es menor o igual a 20")

if bool(not(x == y)):
    print("x no es igual que y")
else:
    print("x es igual que y")