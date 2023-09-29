import math
base=6
expoente=4
lista=[]

while base>=0:
    lista.append(int(math.pow(base,expoente)))
    lista.append(expoente)
    base-=2
    expoente+=2
print(lista)
