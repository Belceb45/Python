#Construir un programa que, al recibir como datos el peso, la altura y el genero
#de N personas que pertenecen a un estado de un pais, obtenga el promedio del peso y el 
#promedio de la altura, tanto de la poblacion masculina como de la femenina


comprobar=True

while comprobar==True:

    n=int(input("Ingrese la cantidad de personas a estudiar: "))

    if n>0:
            comprobar=False
            peso_hombres=0
            altura_hombres=0
            peso_mujeres=0
            altura_mujeres=0
            cantidad_hombres=0
            cantidad_mujeres=0

            for i in range(n+1):
                
                peso=float(input("Ingrese el peso en Kg: "))
                altura=int(input("Ingrese la altura en Cm: "))
                genero=(input("Ingrese el genero de la persona (M)(F): "))

                if genero.upper()=="M":
                    
                    peso_hombres+=peso
                    altura_hombres+=altura
                    cantidad_hombres+=1
            
                
                elif genero.upper()=="F":
                    
                    peso_mujeres+=peso
                    altura_mujeres+=altura
                    cantidad_mujeres+=1
                
                else:
                    print("La letra seleccionada no es correcta, intente de nuevo")

            
            promedio_pesoH=peso_hombres/cantidad_hombres
            promedio_alturaH=altura_hombres/cantidad_hombres
            promedio_pesoM=peso_mujeres/cantidad_mujeres
            promedio_alturaM=altura_mujeres/cantidad_mujeres
            print("De los datos recogidos los promedio son:"
                    "\nPromedio peso de hombres: ",promedio_pesoH,
                    "\nPromedio altura de hombres: ",promedio_alturaH,
                    "\nPromedio peso mujeres:",promedio_pesoM,
                    "\nPromedio altura de mujeres:",promedio_alturaM)
    else:
        print("El numero genera error, vuelve a intentar")