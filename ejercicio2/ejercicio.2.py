# programa para una parte de un video juego

# librerías
import random

# input

print("------------------")
print("----cuidado con el dragón----")
print("------------------")

# processing and output

c=random.randint(1,50)
Hp=int(input("digite el valor de tu vida que es 50: "))
while True:
    print("el dragon te quemo:" +str(c))
    Hp=Hp-c
    c=random.randint(1,50)
    if Hp <= 0:
        break
print("game over")