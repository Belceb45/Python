#Realizar un programa que, al recibir informacion como dato entero
#positivo N, calcule el resultado de la siguiente serie:

#1/(1/2)*(1/3)* ... (*/)(1/N)
#Si el usuario escribe un numero incorrecto, el programa no se ejecuta. 
#En cambio, pregunta de nuevo por la informacion hasta que el dato ingresado
#sea el correcto.

#Usando WHILE


comprobar=True
while comprobar==True:

    n=int(input("Ingrese un numero para la serie: "))

    if n>0:
        comprobar=False
        resultado=1
        i=2
        while i<=n:
            if i % 2==0:
                resultado=resultado/(1/i)
                #print("Es impar")
            else:
                resultado=resultado*(1/i)
            i+=1
        print("El resultado es: ",resultado)
    else:
        print("El numero genera error, vuelve a intentar")