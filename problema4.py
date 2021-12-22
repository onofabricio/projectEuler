
aux = 0
for i in range(100,1000):
    for j in range(100,1000):
        n = i*j
        m = str(n)[::-1]
        if str(n) == m and n > aux:
               aux1 = i
               aux2 = j
               aux = n


print('{} x {} = {}'.format(aux1,aux2,aux))


