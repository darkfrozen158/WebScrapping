cadena = "Hola Mundo"

x = len(cadena)

print(x)
print(cadena[0])
print(cadena[9])

print("----------------------------")

for c in cadena:
    print(c)


print("----------------------------")

print(cadena.lower())

print("----------------------------")

print(cadena.upper())

print("----------------------------")

print(cadena.startswith("Hola"))

print("----------------------------")

print(cadena.startswith("bola"))

print("----------------------------")

print(cadena.endswith("Mundo"))

print("----------------------------")

print(cadena.isdigit())

print("----------------------------")

print(cadena.isnumeric())

print("----------------------------")

print(cadena.strip())

print("----------------------------")

frutas = "Durazno, Manzanas, Papayas"

print(frutas)
print("----------------------------")

print(frutas.split(","))
print("----------------------------")

lista = frutas.split(",")

print("----------------------------")

print(lista)
lista2 = "_".join(lista)

print("----------------------------")

print(lista2)