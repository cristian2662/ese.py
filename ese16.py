import math
import os


n=int(input("inserisci un numero (>0): "))
#r= math.sqrt(n)
#print(r)

try: 
    a=int(n)
except ValueError:

    print("non è un intero ")
    os._exit(1)

if a>0:
    r= math.sqrt(a)
    print ("radice quadrata" +str(r))
else:
    print("non è maggiore di 0")