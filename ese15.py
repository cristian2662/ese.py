import math

x1=int(input("insersici il punto x1: "))
y1=int(input("insersici il punto y1: "))
print(" il primo punto: ("+str(x1)+","+str(y1)+")")

x2=int(input("insersici il punto x2: "))
y2=int(input("insersici il punto y2: "))
print(" il secondo punto: ("+str(x2)+","+str(y2)+")")

E= math.sqrt( math.pow(x1-x2,2)+math.pow(y1-y2,2))
print("distanza euclidea: " +str(E))

