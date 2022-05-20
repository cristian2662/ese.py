input1=input('lato a:\t')
input2=input('lato b:\t')

a=int(input1)
b=int(input2)

for riga in range(0, b):
    if riga ==0 or riga==(b-1):
        for colonna in range(0, a):
            print('* ', end='')
        print('\n', end='')
    else:
        for colonna in range(0, a):
            if colonna ==0 or colonna ==(a-1):
                print('* ', end='')
            else:
                print('  ', end='')
        print('\n', end='')
            