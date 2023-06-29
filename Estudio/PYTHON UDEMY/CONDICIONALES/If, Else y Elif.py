#Condicionales:
    #Los condicionales nos ayudan a crear diferentes eventos
    #y situaciones que apartir de una condicion se va a ejecutar 
    # de una manera u otra

# IF: "Si....", pero de condicion, no de afirmacion
# ELSE: "Si no se cumple la condicion", 

#ELIF: Sirve para anidar diferentes condiciones


#Ejemplo de IF-ELSE
#NOTA: es importante identar de forma correcta, usando 
# ":" para cerrar el condicional
# x=int(input("¿Cuál es tu edad?: "))
# if x>=18:
#     print("Tienes acceso a tu DNI")
# else:
#     print("No tienes acceso a tu DNI")

#Ejemplo de ELIF:
#NOTA: Es importante identar bien

x=str(input("Letra: "))  

if x.lower()=="a":
    print("Esta es la vocal A")
elif x.lower()=="e":
    print("Esta vocal es la E")
elif x.lower()=="i":
    print("Esta vocal es la I")
elif x.lower()=="o":
    print("Esta vocal es la O")
else:
    print("Esta vocal es la U")


#Ejemplo de COndicionales anidados

# y=str(input("Nombre: "))
# d=int(input("Clave: "))

# if y=="Diego":
#     if d==2003:
#         print("Nombre y clave correctos, puedes ingresar")
#     else:
#         print("Clave incorrecta")
        

# else:
#     print("Incorrecto. \n 2 intentos restantes")