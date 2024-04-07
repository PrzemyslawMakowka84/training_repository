str_input = input('Podan ciąg znaków: ')
if not str_input.isupper():
    str_input = str_input.upper()
    print(str_input)

print(f'{str_input.find("ISA ") = }')
if str_input.find('ISA') != -1:
    print('Text zawiera ciąg ISA')
if str_input[0:2] == 'SN':
    print("Pierwsze dwa znaki to SN")