from random import randint

if __name__ == '__main__':
    start = 0
    end = 10
    com = randint(start, end)
    n = 0
    x = 0
    czy_grac_dalej = True
    ilosc_prob = 3
    while czy_grac_dalej and n < ilosc_prob:
        x = int(input(f'Podaj liczbę z przedziału <{start}, {end}>: '))
        if x > com:
            print('Podana liczba jest mniejsza od wylosowanej! Spróbój jeszcze raz!')
        elif x < com:
            print('Podana liczba jest wieksza od wylosowanej! Spróbój jeszcze raz!')
        elif x == com:
            czy_grac_dalej = False
        n += 1

    if n <= ilosc_prob:
        print(f'Wygrana, odgadłeś po {n} próbach! - {com} to wylosowana liczba')
    else:
        print(f'Nie udalo się spróbój jeszcze raz! Wylosowana liczba to {com}')