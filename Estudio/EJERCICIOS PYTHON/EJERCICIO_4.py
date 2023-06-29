#Realizar un programa que, al recibir informacion como dato entero
#positivo N, calcule el resultado de la siguiente serie:

#1+(1/2)+(1/3)+ ... +(1/N)
#Si el usuario escribe un numero incorrecto, el programa no se ejecuta. 
#En cambio, pregunta de nuevo por la informacion hasta que el dato ingresado
#sea el correcto.
 
#USANDO WHILE

comprobar=True
while comprobar==True:

    n=int(input("Ingrese un numero para la serie: "))

    if n>0:
        comprobar=False
        resultado=0
        i=1
        while i<=n:
            resultado+=(1/i)
            i+=1
        print(resultado)
    else:
        print("El numero genera error, vuelve a intentar")