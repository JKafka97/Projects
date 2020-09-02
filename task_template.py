'''
author = 
'''
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
garpike and stingray are also present.''']

#splitter = "-"*40
#print(splitter)
#print("Welcome to the app. Please log in: ")
#user_name = input("USERNAME: ")
#user_password = input("PASSWORD: ")
#print(splitter)
#log = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
#if user_name not in log.keys() and log[user_name] != user_password:
    #quit
#print("We have 3 texts to be analyzed.")
number = int(input("Enter a number btw. 1 and 3 to select: "))
split_words = TEXTS[number-1].split()
words = len(split_words)
title = 0
upper = 0
lower = 0
numeric = 0
calculate = 0
while calculate != words:
    if split_words[calculate].istitle():
        title += 1
    elif split_words[calculate].isupper():
        upper += 1
    elif split_words[calculate].islower():
        lower += 1
    elif split_words[calculate].isnumeric():
        numeric += 1
    calculate += 1

if number == 1:
    print("There are {} words in the selected text".format(words))
    print("There are {} titlecase words".format(title))
    print("There are {} uppercase words".format(upper))
    print("There are {} lowercase words".format(lower))
    print("There are {} numeric strings".format(numeric))
if number == 2:
    print("There are {} words in the selected text".format(words))
    print("There are {} titlecase words".format(title))
    print("There are {} uppercase words".format(upper))
    print("There are {} lowercase words".format(lower))
    print("There are {} numeric strings".format(numeric))
if number == 3:
    print("There are {} words in the selected text".format(words))
    print("There are {} titlecase words".format(title))
    print("There are {} uppercase words".format(upper))
    print("There are {} lowercase words".format(lower))
    print("There are {} numeric strings".format(numeric))
