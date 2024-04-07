# temp = float(input('Podaj temperature: '))
# if 36.5 <= temp <= 36.8:
#     print('Norma')
# elif temp < 36.5:
#     print('Wychłodzenie')
# else:
#     print('Gorączka!')

wynik = float(input('Podaj liczbę punktów: '))
procent = wynik / 50 * 100
if 50 >= wynik >= 0:
    if procent >= 0.91 or procent == 1.0:
        print(f'Ocena 5 - {procent:.0f}%')
    elif 0.71 <= procent <= 0.90:
        print(f'Ocena 4 - {procent:.0f}%')
    elif 0.51 <= procent <= 0.70:
        print(f'Ocena 3 - {procent:.0f}%')
    elif 0.0 <= procent <= 0.50:
        print(f'Ocena 2 - {procent:.0f}%')
else:
    print('Podano za duzy lub mały wynik!')