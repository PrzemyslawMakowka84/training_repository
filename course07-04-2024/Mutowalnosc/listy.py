n = 0
list1 = []
while n < 10:
    x = int(input('Podaj liczbe: '))
    list1.append(x)
    n += 1
for i in range(0, len(list1)):
    print(f'2 ** {list1[i]} = {2 ** list1[i]}')

lista_ocen = []
lista_dostępnych_ocen = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
n = 0
while n < 5:
    ocena = float(input('Podaj ocene: '))
    if ocena in lista_dostępnych_ocen:
        lista_ocen.append(ocena)
        n += 1
    else:
        print('Podałeś nieprawidłową ocenę! Spróbój jescze raz')

srednia = 0.0
for i in lista_ocen:
    srednia += i

print(f'Średnia ocena = {srednia / n}')

lista_wystapien = [1, 2, 5, 6, 3, 2, 4, 6]
szukane_wystapienie = 6
x = lista_wystapien.count(szukane_wystapienie)
index = 0
for i in range(0, len(lista_wystapien)):
    if szukane_wystapienie == lista_wystapien[i]:
        index = i

if x > 0:
    print(f'liczba 6 występuje pod indeksem: {index}')
else:
    print("Brak wystąpienia")