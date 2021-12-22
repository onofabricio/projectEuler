for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a*a + b*b == c*c and a<b and b<c:
                #pitagpric triplet
                suma = a+b+c
                if suma == 1000:
                    produto = a*b*c
                    break
print("{}² + {}² = {}²".format(a,b,c))
print("a+b+c= ", produto)
#com a e b = 500 , resposta = 248751999
#com a e b = 800 , resposta = 637762599

