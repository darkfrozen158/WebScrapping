#MODOS : "r" -> "leer archivo" , "a" -> "agregar " , "w" -> "escribir archivo"

f = open("archivos/archivo2.txt", "r")

#STRIP ES PARA QUITAR LOS SALTOS DE LINEA

for i in f:
    i = i.strip()
    i = i.split(",")
    print(i)
    print("---")
    print(i[0])
    print("---")
    print(i[1])
    print("---")
    print(i[2])
    print("---")

a = open("archivos/archivo2.txt", "a")

a.write("Guayaba,50,50\n")


w = open("archivos/archivo3.txt","w")

w.write("Hiii")




