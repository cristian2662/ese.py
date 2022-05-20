while True:
    input1 = input('Altezza: ')
    try:
        x = int(input1)
    except:
        pass
    if x>0 or x<=9:
        break;
        
cont =0
for riga in range(1, x + 1):
        for colonna in range(1, x - riga + 1):
            print(' ', end='')
            
        cont =1
        for j in range ( x - riga + 1, x + 1):
            print(str(cont), end='')
            cont = cont +1
        cont=riga-1
        for j in range(x - riga + 2, x + 1):
            print(str(cont), end='')
            cont =cont-1
        print('\n', end='')