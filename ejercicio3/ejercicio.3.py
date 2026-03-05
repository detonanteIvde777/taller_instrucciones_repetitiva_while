import random

numero= random.randint(1,100)
intentos=0

while intento  != numero:
    intento=int(input("adivina el numero entre 1 y 100: "))

    if intento < numero:
        print("el numero es mas alto")

    if intento > numero:
        print("el numero es mas bajo")

print("FELICIDADES HA ADIVINADO EL NUMERO :)")