#Ejemplos booleanos
print(10>2 and 10>=11)
print(10>2 or 10>=11)
print(not 12>=11 and 10<=11)

#Metodos booleanos

cadena="Metodos Booleano para las strings"
cadena2="HOLA"
cadena3="hola"
#startswith
# Nos sirve para verificar si la cadena inicia con el digito indicado
print(cadena.startswith("R"))

#endswith
#Es lo contrario de startswith
print(cadena.endswith("S"))

#isupper sirve para verificar si todo esta en mayus
print(cadena2.isupper())
#islower es lo contrario a isupper
print(cadena3.islower())