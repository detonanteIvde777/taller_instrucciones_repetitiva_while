# programa para imprimir en cuantos meces, uniendo los dos capitales, se llega a un valor mayor a c3 

#------------------
# librerias
import math


#------------------
# input
print("-------------------")
c1=float(input("ingrese el capital de pedro: "))
c2=float(input("ingrese el capital de juan: "))
print("-------------------")

#------------------
# processing
n=0
while True:
    c1=c1+(c1*0.03)
    c2=c2+(c2*0.04)
    n=n+1
    if (c1+c2)>1000000:
        break

#------------------
# output
print("-------------------")
print("RESULTADOS")
print("-------------------")
print("unidos  los dos capitales de ambos socios, puedes hacer el negocio que desean despues de: " +str(n)+" meses")
print("--------------------")  
print("fin de programa")
print("--------------------")
