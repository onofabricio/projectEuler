# 2

fibonacci = []

aux1 = 1
aux2 = 2

for i in range(30):
    aux3 = aux1 + aux2

    fibonacci.append(aux3)
    aux1 = aux2
    aux2 = aux3

    i = i + aux3
print(fibonacci)
suma =0
for j in range(30):
    if fibonacci[j] % 2 == 0:
        suma = suma + fibonacci[j]

print(suma+2)
