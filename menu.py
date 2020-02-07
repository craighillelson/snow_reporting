""" __doc__ """

# menu

import os

RTN = lambda: '\n'

entries = os.listdir()
choices_lst = []
options = []
choices_dct = {}
alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

for file in sorted(entries):
    if '.py' in file and 'functions' not in file and 'menu' not in file:
        choices_lst.append(file)

i = 0

for choice in choices_lst:
    choices_dct[f'{alphabet[i]}.'] = choices_lst[i]
    options.append(alphabet[i])
    i += 1

print(RTN())

while True:
    try:
        print('please make a selection')
        for letter, script in choices_dct.items():
            print(letter, script)
        usr_choice = input()
        if usr_choice not in options:
            print('not one of the options\n')
        else:
            break
    except ValueError:
        print('invalid input')

print(RTN())
