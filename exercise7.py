# funktion buchstaben zählen, die Buchstaben in string zählt
def buchstaben_zählen(x): # Funkion definieren, x steht für Wort oder text
    x_list = list(x)  # spliten der stings,in gewünsche und ungewünschte elemente, funktion list zählt alles auf
    x_buchstaben = [i for i in x_list if i.isalpha()]  # jetzt Buchstaben zählen, hier List komprehension, kann aber umgeschrieben werden mit for schleife und . append
    x_buchstaben_len = len(x_buchstaben)  # funktion zum länge bestimmen
    return x_buchstaben_len

print(buchstaben_zählen("Hallo Berlin!"))



#for   # jedes element im String prüfen --> for schleife
