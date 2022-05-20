import math

while True:
    input1 = input('inserire un intero > 0: ')
    try:
        x = int(input1)
    except ValueError:
        print(input1 + " non è un intero ")
    if x>0:
        break;

y = x
cont =0
while y>0:
    y = y //10
    cont = cont +1

acc=x
i=cont
while i>0:
    v = acc//math.pow(10., i-1);
    print(str(int(v))+ ' ', end='')
    j=0
    while j < v:
        print(' ', end='')
        j = j +1
    print('\n', end='')
    acc %= int(math.pow(10., i-1))
    i = i-1