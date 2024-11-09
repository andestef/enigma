from random import choice
from json import dumps
gen = input("Gen: ")
def generate(gen):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    data = {}
    if gen == "plugboard":
        for i in range(1,10):
            x = choice(alphabet)
            alphabet.remove(x)
            y = choice(alphabet)
            alphabet.remove(y)
            data[x] = y
        for i in alphabet:
            data[i] = i
        open('sets/plugboard.json','w').write(dumps(data,indent=4))
    elif gen == 'current_settings':
        validnumbers = list(range(1,26))
        open('sets/rotors/current_settings.json','w').write(dumps([choice(validnumbers),choice(validnumbers),choice(validnumbers)],indent=4, sort_keys=True))
    elif gen == 'a' or gen == 'b' or gen == 'c' or gen == 'reflector':
        for a in list(alphabet):
            c = choice(alphabet)
            data[a] = c
            alphabet.remove(c)
        if gen == 'reflector':
            open('sets/'+gen+'.json','w').write(dumps(data,indent=4, sort_keys=True))
        else:
            open('sets/rotors/'+gen+'.json','w').write(dumps(data,indent=4, sort_keys=True))
if gen == 'all':
    for i in ['a','b','c','current_settings','reflector',"plugboard"]:
        generate(i)
else:
    generate(gen)