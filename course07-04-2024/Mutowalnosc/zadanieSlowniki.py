ksiazka_telefoniczna = {}
opcja = 'D'
while True and opcja != 'W':
    opcja = input("'D' - dodaj numer do ksiązki, 'Z' - Zamien numer. 'U' - usun numer: ")
    match opcja:
        case 'D':
            imie = input('Podaj imie: ')
            numer = int(input('Podaj numer: '))
            ksiazka_telefoniczna[imie] = numer
        case 'Z':
            if len(ksiazka_telefoniczna) == 0:
                print('Ksiązka jest pusta! Edycja niemożliwa!')
            else:
                print(ksiazka_telefoniczna)
                imie = input('Podaj wartość jaką chcesz edytować: ')
                if imie in ksiazka_telefoniczna.keys():
                    numer = int(input('Podaj numer: '))
                    ksiazka_telefoniczna[imie] = numer
                else:
                    print('Brak podanego imienia!')
        case 'U':
            if len(ksiazka_telefoniczna) == 0:
                print('Ksiązka jest pusta! Edycja niemożliwa!')
            else:
                print(ksiazka_telefoniczna)
                imie = input('Podaj wartość jaką chcesz usunac z kisązki')
                if imie in ksiazka_telefoniczna.keys():
                    ksiazka_telefoniczna.pop(imie)
                else:
                    print('Brak podanego imienia!')
    print(ksiazka_telefoniczna)