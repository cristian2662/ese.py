
#primavera 4 6
#estate 7 9
#inverno 1 3
#autunno 10 12
n=int(input("inserisci il mese compreso tra 1 e 12: "))
m=int(input("inserisci il giorno del mese: "))

#if  n>12 or n<0:
 #print("numero non valido, riprovare")
if n<=0 or n>12:
   print("mese non valido, riprovare")
   
if n==12 and  m>21 or n==3 and m<20:
    print("siamo in inverno")
if n==12 and m<21 or n==9 and m>23:
    print("siamo in autunno") 
if n==6 and m>21 or n==9 and m<23:
    print("siamo in estate")
if n==3 and m>20 or n==6 and m<21:
    print("siamo in primavera")