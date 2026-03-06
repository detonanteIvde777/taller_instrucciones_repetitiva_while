# programa para calcular cuantas veses rebota la pelota

#------------------
# librerias
#------------------
import math

#------------------
# input
#------------------

print("-------------------")
print("-----pelota saltarina")
print("-------------------")
h=int(input("ingrese la altura desde la que se deja caer la pelota (en metros): "))
l=h/5
n=0

#------------------
# processing
#------------------

while True:
    h=h-(h*0.10)
    n=n+1
    if h<l:
        break

#------------------
# output
#------------------

print("-------------------")
print("RESULTADOS")
print("-------------------")
print("la pelota llego a menos de 1/5 de la altura inicial despues de rebotar: " +str(n)+" veces")