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

splitter = "-"*40
print(splitter)
print("Welcome to the app. Please log in: ")
user_name = input("USERNAME: ")
user_password = input("PASSWORD: ")
print(splitter)
log = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
if user_name not in log.keys() and log[user_name] != user_password:
    quit
print("We have 3 texts to be analyzed.")
number = int(input("Enter a number btw. 1 and 3 to select: "))
print(splitter)

text_no_comma = str(TEXTS[number-1]).replace(",", "")
text_no_dot = text_no_comma.replace(".", "")
split_words = text_no_dot.split()
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
print(splitter)
word_1 = 0
word_2 = 0
word_3 = 0
word_4 = 0
word_5 = 0
word_6 = 0
word_7 = 0
word_8 = 0
word_9 = 0
word_10 = 0
word_11 = 0
word_12 = 0
word_13 = 0
word_14 = 0
word_15 = 0

calculate = 0
while calculate != words:
    if len(split_words[calculate]) == 1:
        word_1 += 1
    elif len(split_words[calculate]) == 2:
        word_2 += 1
    elif len(split_words[calculate]) == 3:
        word_3 += 1
    elif len(split_words[calculate]) == 4:
        word_4 += 1
    elif len(split_words[calculate]) == 5:
        word_5 += 1
    elif len(split_words[calculate]) == 6:
        word_6 += 1
    elif len(split_words[calculate]) == 7:
        word_7 += 1
    elif len(split_words[calculate]) == 8:
        word_8 += 1
    elif len(split_words[calculate]) == 9:
        word_9 += 1
    elif len(split_words[calculate]) == 10:
        word_10 += 1
    elif len(split_words[calculate]) == 11:
        word_11 += 1
    elif len(split_words[calculate]) == 12:
        word_12 += 1
    elif len(split_words[calculate]) == 13:
        word_13 += 1
    elif len(split_words[calculate]) == 14:
        word_14 += 1
    elif len(split_words[calculate]) == 15:
        word_15 += 1
    calculate += 1

if word_1 != 0:
    print("1", "*" * word_1, word_1)
if word_2 != 0:
    print("2", "*" * word_2, word_2)
if word_3 != 0:
    print("3", "*" * word_3, word_3)
if word_4 != 0:
    print("4", "*" * word_4, word_4)
if word_5 != 0:
    print("5", "*" * word_5, word_5)
if word_6 != 0:
    print("6", "*" * word_6, word_6)
if word_7 != 0:
    print("7", "*" * word_7, word_7)
if word_8 != 0:
    print("8", "*" * word_8, word_8)
if word_9 != 0:
    print("9", "*" * word_9, word_9)
if word_10 != 0:
    print("10", "*" * word_10, word_10)
if word_11 != 0:
    print("11", "*" * word_11, word_11)
if word_12 != 0:
    print("12", "*" * word_12, word_12)
if word_13 != 0:
    print("13", "*" * word_13, word_13)
if word_14 != 0:
    print("14", "*" * word_14, word_14)
if word_15 != 0:
    print("15", "*" * word_15, word_15)
print(splitter)
sum_of_all_number = 1 * word_1 + 2 * word_2 + 3 * word_3 + 4 * word_4 + 5 * word_5 + 6 * word_6 + 7 * word_7 + 8 * word_8 + \
       9 * word_9 + 10 * word_10 + 11 * word_11 + 12 * word_12 + 13 * word_13 + 14 * word_14 + 15 * word_15
print("If we summed all the numbers in this text we would get: {}".format(float(sum_of_all_number)))
print(splitter)
