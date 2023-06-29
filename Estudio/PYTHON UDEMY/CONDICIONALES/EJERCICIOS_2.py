#EJERCICIO 1

x1=input("Primera palabra: ")
x2=input("Segunda palabra: ")

if len(x1)<3 or len(x2)<3:
    print("NO rima, porque tiene menos de 3 caracteres.")
elif x1[-3:] == x2[-3:]:
    print("Las palabras riman")
elif x1[-2:]==x2[-2:]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")

#Ejercicio 2

print("Candidatos: \n A_Partido Rojo \n B_Partido Verde \n C_Partido Azul \n Escoger el candidato de preferencia con base a la letra A,B o C")

eleccion=str(input("\n Candidato : "))
 
if eleccion.upper()=="A":
    print("Usted ha votado por el partido ROJO.")
elif eleccion.upper()=="B":
    print("Usted ha votado por el partido VERDE.")
elif eleccion.upper()=="C":
    print("Usted ha votado por el partido AZUL.")
else:
    print("Opción Errónea.")