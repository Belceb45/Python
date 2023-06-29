#Rubio Haro Diego- CALCULO
#Ejemplo de implementación del método de Ne6
import numpy as np
import math
# INGRESO
fx  = lambda x: math.cos(x)-x
dfx = lambda x: -math.sin(x)-1

fx2  = lambda x: x**6-2
dfx2 = lambda x: 6*x**5



xi=int(input("Ingrese el valor inicial de x0: "))
iteraciones=0
cont=xi

# PROCEDIMIENTO
lista = []
while (iteraciones<20):
    xnuevo = xi - fx(xi)/dfx(xi)
    xi=xnuevo
    lista.append(xi)
    iteraciones=iteraciones+1

# convierte la lista a un arreglo.

# SALIDA
print("\n",*lista,sep="\n")
print('\nraiz en: ', xi)

