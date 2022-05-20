
import os
while True:
    a=input("inserisci un vlaore intero: ")
    val=True
  
   
    try: 
        if a<0:  
            print("numero negativo") 
        a1=int(a)
    except ValueError:
        print(str(a) + ": non è un intero")
        val=False
    if val:
        break

i=0
while i<a1:
    print("*",end="")
    i=i+1
print("\n", end="")
print("finito")