import matplotlib.pyplot as plt

def buchstaben_häufigkeit(x):
    mein_d = {} # leeres dictionary erstellen ,it {}
    
    for b in x.lower():  #forschleife starten: für jedes element b in der Eingabe x, Eingabe soll klein geschrieeben werden
        if b.isalpha():  # wenn element aus der Zeichenkette die wir eingeben wirklich ein Buchstabe ist
            if b not in mein_d:  # wenn buchstabe noch nicht da ist (im dictionary) 
                mein_d[b] =1 # dann speichere diesen Buchstabe in mein dictionary und dazu speichere auch den wert 1
                            # Eintragung in Dictionary mit [  ], b ist Schlüssel, 1 = value in dictionary
            else:
                mein_d[b]+=1 # ansonsten wenn buchstabe schon existiert, dann wollen wir eine 1 addieren (für B zählen)
                
    mein_d_sorted = dict(sorted(mein_d.items())) # dictionary alphabetisch ordnen mein_d ist ursprüngl dictionary
    
    return mein_d_sorted  # ausgeben der function, ende der Funktion, was sie zurückgibt

# print(buchstaben_häufigkeit(x = "123Wie g&eht es Ihnen%$?"))  # werte eingeben und printen

# Ergebnisse der Funktion irgendwo , in bh_dict1 dictionary speichen, damit funktion auch was zurückgeben kann, 
#wenn man es druckt wird es nur visualisiert aber nicht gespeichert

bh_dict1= (buchstaben_häufigkeit(x = "123Wie g&eht es Ihnen%$?"))
bh_dict2= (buchstaben_häufigkeit(x = "Hallo Berlin"))


# barplot erstellen
plt.bar(bh_dict1.keys(), bh_dict1.values())

