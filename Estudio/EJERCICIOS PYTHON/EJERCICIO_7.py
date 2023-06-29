#Construye un programa que, al recibir como datos N numeros naturales, determine
#cuantos de ellos son positivos, negativos o nulos.

#Si el usuario escribe un numero incorrecto, el programa no se ejecuta.
#En cambio, pregunta d enuevo por la informacion hasta que el dato ingresado
#sea correcto

#USANDO FOR

comprobar=True
while comprobar==True:

    n=int(input("Ingrese la cantidad de datos que desea procesar: "))

    if n>0:
        comprobar=False
        postivo=0
        negativo=0
        nulos=0

    for i in range(n):   
        dato=int(input("Ingrese el numero natural: "))
        if dato >0:
            postivo+=1
        elif dato <0:
            negativo +=1
        else:
            nulos +=1

    print("La cantidad de numeros postivos fue: ",postivo)
    print("La cantidad de numeros negativos fue: ",negativo)
    print("La cantidad de numeros nulos fue: ",nulos)

else:
    print("El numero genera error, vuelve a intentar")