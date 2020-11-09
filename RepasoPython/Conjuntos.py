conjunto = {1,5,9}

conjunto.add(10)

print(conjunto)

conjunto.add(9)

print(conjunto)

conjunto.remove(9)

print(conjunto)

for i in conjunto:
    print(i)


print(5 in conjunto)

conjunto1 = {1,5,9}
conjunto2 = {1,5,10}

print(conjunto1.union(conjunto2))