import math

a=int(input("insersici un numero: "))
b=int(input("insersici un numero: "))
c=int(input("insersici un numero: "))

if a>b or a>c:
   max=int (a)
   
if b>a or b>c:
   max=int(b)
   
if c>a or c>b:
   max=int(c)
   
print("numero massimo: "+str(max))

if a<b or a<c:
    min=int(a)
if b<a or b<c:
    min=int(b)
if c<a or c<b:
    min=int(c)

print ("numero minimo: "+str(min))
somma=a+b+c
media=somma/3

print("la media è: "+str(media))
r= math.sqrt(somma)
print("la radice della somma è: "+str(r))