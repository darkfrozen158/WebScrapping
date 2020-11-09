d = { "edad": 10,
      "nombre": "Leo"
}

print(d)

print(d["edad"])


d["Ciudad"] = "Lima"

print(d)

del d["Ciudad"]

print(d)

d["edad"] = 20

print(d)

d["edad"] = d["edad"]  + 20

print(d)


print("______________________________________")


#RECORRER DICCIONARIO :

for k, v in list(d.items()):
    print(k,v)


#DICCIONARIO ANIDADO :


e = {
    "nombre": ["Hola Mundo", 19],
    "edad": {
        "edad padre": "54",
        "nombre padre": "Carlos"
    }

}

print(e)

print(e["nombre"][1])
print(e["edad"]["edad padre"])