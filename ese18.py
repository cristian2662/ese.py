#primavera 4 6
#estate 7 9
#inverno 1 3
#autunno 10 12
n=int(input("inserisci un numero compreso tra 1 e 12: "))

#if  n>12 or n<0:
 #print("numero non valido, riprovare")
if n<=0 or n>12:
   print("numero non valido, riprovare")
if n>=1 and n<=3:
    print("siamo in inverno")
elif n>=4 and n<=6:
    print(" siaamo in primavera")
elif n>=7 and n<=9:
    print("siamo in estate")
elif n>=10 and n<=12:
    print("siamo in iautunno")
