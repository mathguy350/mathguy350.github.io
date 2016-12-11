#!/usr/bin/env python3

import colors as c
from string import ascii_lowercase as s
import time as t
print(c.o + "Welcome to the Cipher" + c.x)

code = {
        "a": "+",
        "b": "-",
        "c": "@",
        "d": "%",
        "e": "&",
        "f": "$",
        "g": "#",
        "h": "^",
        "i": "*",
        "j": "(",
        "k": ")",
        "l": "_",
        "m": "=",
        "n": "[",
        "o": "]",
        "p": "{",
        "q": "}",
        "r": "/",
        "s": "<",
        "t": ">",
        "u": ",",
        "v": ".",
        "w": "?",
        "x": "!",
        "y": ";",
        "z": ":",
        " ": " "
}

decoder  = {y:x for x,y in code.items()}

def encode(msg):
    for char in msg.lower():
        enc = code[char]
        print(c.base3 + enc, flush = True, end = "")
        t.sleep(0.25)
    print()    

def decode(msg):
    global holder
    holder = ""
    print(c.multi("A complex calculation is about to be initiated..."))
    for char in msg:
        dec = decoder[char]
        holder += dec
        decode2(dec)
    print(c.clear + c.random() + "Your decoded message is " + c.base3 + holder)
def decode2(char):
    for letter in " " + s:
        print(c.random() + letter,flush = True, end = "")
        t.sleep(0.1)
        if letter == char:
            print()
            print(c.random() +  "So far, we have found " + holder)
            t.sleep(1)
            print(c.clear)
            break
        else:
            continue
def asdf():
    for key, value in sorted(code.items()):
        print(key + " goes to " + value)

def ask():
    decision = input("Do you want to print the key to this program (P)? Or do you want to encode or decode a message (E or D): ")
    return decision

def e_d(decision):
    if decision.lower() == "e":
        message = input("Enter a message to encode: ")
        encode(message)
    elif decision.lower() == "d":
        message = input("Enter a message to decode: ")
        decode(message)
    elif decision.lower() == "p":
        asdf()
    else:
        e_d(ask())

print(c.clear)
x = ask()
e_d(x)
