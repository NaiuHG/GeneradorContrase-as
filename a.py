#Creador : https://www.facebook.com/TioNayuCH

from random import choice
from string import ascii_letters , digits
import os
import sys
print ("   Creador: https://www.facebook.com/TioNayuCH   ")

print ("   Que disfrutes el generador :)   ")

print ("   Cual quiera error que encuentres favor de mandarlo a mi facebook   ")

print ("   Cual quier duda a mi facebook que disfrutes el GENERADOR :)   ")


try:
    os.system('clear')
except:
    os.system('cls')
    
longitud = int(input(" Longitud de la contraseña: ")) 
cuantas = int(input(" Cuantas Contraseñas desean Generar: "))
caracteres = ascii_letters + digits
def generador(ab):
    for i in range(ab):
        final = ''.join([choice (caracteres) for i in range(longitud)])
        print (final)
generador(cuantas)
