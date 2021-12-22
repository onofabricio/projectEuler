vec = []
cont = 0
for i in range(1000):
    if 0 == i % 3 or 0 == i%5:
        cont = cont + i


print('soma =',cont)

