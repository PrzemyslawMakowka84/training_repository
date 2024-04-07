for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
        print('Pif Paf')
    elif x % 3 == 0:
        print('Pif')
    elif x % 5 == 0:
        print('Paf')
    else:
        print('Miss')

n = int(input('Podaj liczbe: '))
for i in range(n+1):
    print('*' * i)
