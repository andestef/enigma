import json
import keyboard
a = json.load(open('sets/rotors/a.json'))
b = json.load(open('sets/rotors/b.json'))
c = json.load(open('sets/rotors/c.json'))
current_settings = json.load(open('sets/rotors/current_settings.json'))
plugboard = json.load(open('sets/plugboard.json'))
reflector = json.load(open('sets/reflector.json'))
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def get(ring,letter):
    if ring == 'a':
        
def encode(letter):
    
while True:
    key = keyboard.read_key()
    if key:
        if key in alphabet:
            encode(key)