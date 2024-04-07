language = input('Choose a language: ')

match language:
    case 'PL':
        print('PL language was chosen')
    case 'EN':
        print('EN language was chosen')
    case 'DE':
        print('DE language was chosen')
    case 'FR':
        print('FR language was chosen')
    case 'CZ':
        print('CZ language was chosen')
    case 'ND':
        print('ND language was chosen')
    case _:
        print('Not recognized language')