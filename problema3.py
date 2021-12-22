
n = int(input())
i = 1
aux = 0
while n > 1:
    if n % i == 0:
       aux = i
       n = n/i
    i = i + 1

print(aux)


