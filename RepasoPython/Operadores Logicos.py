from random import *

x = randint(1,5)

if ( x ==1):
    print("Hola Soy el numero 1")
elif (x==2):
    print("Hola soy el numero 2")
else:
    print("Hola soy otro numero")


x = 0

for i in range(10):
    print(i)
    x = x+randint(1,5)

print(x)



y = 0
while (y!=5):
  print( randint(1, 10) )
  break

print(y)

# BREAK -> ROMPER BUCLE
# CONTINUE -> SEGUIR BUCLE




