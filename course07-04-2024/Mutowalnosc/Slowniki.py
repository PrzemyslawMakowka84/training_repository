example = \
    {
        'Adam': 53534534,
        'Ewa': 435345345,
        'Jakub': 2342344
    }
print(example)
test = example.get('dupa', 'brak')
print(test)

example['Dominik'] = 123123123
example['Adam'] = 111111111
print(example.keys())
print(example.items())

for i, j in example.items():
    print(f'{i = } {j = }')
