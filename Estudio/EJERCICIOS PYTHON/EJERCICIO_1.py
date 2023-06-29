#Realizar un programa que te permita generar la tabla de multiplicar
#de un numero entero positivo N, comenzando desde 1.

#Si el usuario escribe un numero incorrecto, el programa no se ejecuta.
#En cambio, pregunta de nuevo por la informacion hasta que el dato 
#ingresado sea correcto.
#Usando FOR

comprobar=True
while comprobar==True:

    n=int(input("Ingrese el numero de la tabla de multiplicar: "))

    if n >0:
        comprobar=False

        for i in range(11):
            print(n, "por",i,"es igual a: ", n*i)
        
    else:
        print("El numero ingresado es incorrecto, vuelve a intentarlo")
    
