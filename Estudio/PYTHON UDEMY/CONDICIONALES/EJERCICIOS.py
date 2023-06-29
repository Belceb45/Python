#EJERCICIO 1

x=str(input("Ingresa una letra: "))

if x.lower() =="a":
     print("Es vocal")
elif x.lower() =="e":
     print("Es vocal")
elif x.lower() =="i":
     print("Es vocal")
elif x.lower() =="o":
     print("Es vocal")
elif x.lower() =="u":
     print("Es vocal")
else:
     print("No es vocal")


#EJERCICIO 2
 
numero=int(input("Ingresa el numero ENTERO: "))

if numero>0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("EL valor absoluto de {} es:".format(numero), numero * -1)
#Tambien se puede usar el metodo abs(x)
