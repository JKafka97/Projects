seznam_clenu=set()
seznam_zaplaceny=set()

otazka=()
while otazka != "":
    otazka = input("Jmeno: ")
    seznam_clenu.add(otazka)
seznam_clenu.remove('')
print(seznam_clenu)

dotaz=()
while dotaz!= "":
    dotaz = input("Jmeno: ")
    seznam_zaplaceny.add(dotaz)
seznam_zaplaceny.remove('')

vsichni = seznam_clenu | seznam_zaplaceny
print("Členové jsou: ",vsichni)
print("Příspěvek zaplatili: ",seznam_zaplaceny)
print("Nezaplatil ", vsichni-seznam_zaplaceny)
