# texty
from typing import List

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# zadani promennych
ODDELOVAC = 30 * "-"
WELCOME = "Vítejte v aplikaci. Prosím použijte Vaše přihlašovací údaje:"
USERS = {"bob":"123", "ann":"pass123", "mike":"password" , "liz":"pass123"}

# uvod
print(ODDELOVAC)
print(WELCOME)
print(ODDELOVAC)

# prihlaseni
keys = USERS.keys()
i = 0
while i >= 0:
    user = input("Zadejte jméno:")
    if user in keys:
        break
    else:
        quit = input("Špatné jméno, přejete si pokračovat?(y/q):")
        if quit == "q":
            exit()
        else:
            print("Zadej znovu")
    i += 1

# overeni hesla
i = 0
while i >= 0:
    password = input("Zadejte heslo:")
    if USERS.get(user) == password:
        break
    else:
        quit = input("Špatné heslo, přejete si pokračovat?(y/q):")
        if quit =="q":
            exit()
        else:
            print("Zadej znovu")
i += 1

# volba textu
print((ODDELOVAC))
print("K dispozici celkem tři texty k otestování.")
choice = int(input("Pro volbu textu k analýze zvolte prosím číslo 1,2 nebo 3:"))-1
print(ODDELOVAC)

# analyza textu
text = TEXTS[choice]
text_clean = [word.strip(",.") for word in text.split()]

# pocet slov
print(f"Počet slov ve zvoleném textu: {len(text_clean)}")

# vystup rozdeleni slov
i = 0
title, upper, lower, numer = 0, 0, 0 ,0
while i < len(text_clean):
    if (text_clean[i]).istitle() == True:
        title += 1
    elif (text_clean[i]).isupper() == True:
        upper += 1
    elif (text_clean[i]).islower() == True:
        lower += 1
    elif (text_clean[i]).isnumeric() == True:
        numer += 1
    i += 1

print(f"Počet slov začínajících velkým písmenem: {title}")
print(f"Počet slov psaných velkým písmem: {upper}")
print(f"Počet slov psaných malým písmem: {lower}")
print(f"Počet číselných hodnot: {numer}")

print(ODDELOVAC)

# graficky vystup
i = 1
word_length = []
while i <= len(text_clean):
    word_length.append(len(text_clean[i - 1]))
    i += 1

keys = list(set(word_length))

i = 1
while i <= len(keys):
    print(keys[i-1], "*" * (word_length.count(keys[i - 1])), word_length.count(keys[i - 1]))
    i += 1

print(ODDELOVAC)

# soucet cisel
i = 0
total_numbers = 0
while i < len(text_clean):
    if (text_clean[i]).isnumeric() == True:
        total_numbers += int(text_clean[i])
    else:
        total_numbers += 0
    i += 1
print(f"Součet všech čísel v textu je:{total_numbers}")

print(ODDELOVAC)


