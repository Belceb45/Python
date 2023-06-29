import random 
from werkzeug.security import generate_password_hash
#Declaración de las variables de caracteres
#Incluir el abecedario en minusc
minus="abcdefghijklmnopqrstuvwxyz"
#Incluir el abecedario en mayusc
mayus=minus.upper()
numeros="0123456789"
simbolos="@(){}[]*,.:;/-_¿?!¡#$%&<>+="
base=minus+mayus+numeros+simbolos
n=int(input("Longitud de la contraseña: "))
longitud=n
#Generar varias claves
for _ in range(10):
    muestra=random.sample(base,longitud)
    password="".join(muestra)
    password_encriptado=generate_password_hash(password)
    print("\n{}-->{}".format(password, password_encriptado))

