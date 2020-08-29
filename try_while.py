
character=input("Write character: ").lower()

list=["Adéla", "Adam", "Adriana", "Adrian", "Agáta", "Albert", "Alena", "Aleš",
      "Alexandra", "Alex", "Alice", "Alexander", "Alžběta", "Alexandr", "Amálie",
      "Andrej", "Amélie", "Antonín", "Andrea", "Benjamin", "Aneta", "Dalibor",
      "Anežka", "Damián", "Anna", "Dan", "Bára", "Daniel", "Barbora", "David",
      "Beáta", "Denis", "Daniela", "Dominik", "Denisa", "Eduard", "Diana", "Eliáš",
      "Dominika", "Erik", "Dorota", "Filip", "Ela", "František", "Elen", "Gabriel",
      "Elena", "Hugo", "Eliška", "Hynek","Ella", "Ivan", "Ellen", "Jáchym", "Ema",
      "Jakub", "Emma", "Jan", "Ester", "Jaromír" ,"Eva", "Jaroslav", "Gabriela",
      "Jindřich", "Hana", "Jiří", "Helena", "Jonáš", "Izabela", "Josef", "Jana",
      "Kamil", "Johana", "Karel", "Jolana", "Kevin", "Josefína", "Kristian", "Julie",
      "Kristián", "Justýna", "Kryštof", "Kamila", "Ladislav", "Karolína", "Libor",
      "Kateřina", "Luboš", "Klára", "Lukáš", "Klaudie", "Marek", "Kristina", "Martin",
      "Kristýna", "Matěj", "Laura", "Matouš", "Lea", "Matyas", "Lenka", "Matyáš", "Leona",
      "Max", "Leontýna", "Maxim", "Liliana", "Maxmilián", "Linda", "Michael", "Lucie", "Michal",
      "Magdalena", "Mikuláš", "Magdaléna", "Milan", "Mariana", "Miroslav" ,"Marie", "Nicolas",
      "Markéta", "Nikolas", "Martina", "Oldřich", "Mia", "Oliver", "Michaela", "Ondřej",
      "Monika", "Oskar", "Natálie", "Patrik", "Nela", "Pavel", "Nella", "Petr", "Nelly",
      "Prokop", "Nicol", "Radek", "Nikol", "Radim", "Nikola", "René", "Nina", "Richard",
      "Patricie", "Robert", "Pavla", "Robin", "Pavlína", "Roman", "Petra", "Rostislav",
      "Rozálie", "Rudolf", "Sabina", "Samuel", "Sandra", "Sebastian", "Sára", "Sebastián",
      "Simona", "Stanislav", "Sofie", "Šimon", "Soňa", "Štěpán", "Stela", "Tadeáš", "Stella",
      "Teodor", "Šárka", "Theodor", "Šarlota", "Tobias", "Štěpánka", "Tobiáš", "Valentýna",
      "Viktor", "Valerie", "Vilém", "Valérie", "Vincent", "Vanesa", "Vít", "Vanessa", "Vítek",
      "Vendula", "Vladimír", "Veronika", "Vojta", "Viktorie", "Vojtěch", "Zuzana", "Zdeněk"]

resault=[]
i=0
while i<len(character):
  for word in list:
    if character[i] in word.lower():
        resault.append(word)
    else: continue
    i+=1
print(resault)
