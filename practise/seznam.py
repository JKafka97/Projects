seznam_clenu=set()
seznam_zaplaceny=set()

otazka=input("Přidal se někdo nový?(ano/ne) ")
while otazka == "ano":
    clen=input("Jmeno: ")
    seznam_clenu.add(clen)
    if clen == "ne":
        seznam_clenu.remove("ne")
        break
print(seznam_clenu)

dotaz=input("Zaplatil někdo?(ano/ne) ")
while dotaz == "ano":
    platce=input("Jmeno: ")
    seznam_zaplaceny.add(platce)
    if platce == "ne":
        seznam_zaplaceny.remove("ne")
        break
vsichni = seznam_clenu | seznam_zaplaceny
print("Členové jsou: ",vsichni)
print("Příspěvek zaplatili: ",seznam_zaplaceny)
print("Nezaplatil ", vsichni-seznam_zaplaceny)

