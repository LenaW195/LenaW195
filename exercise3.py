
def steigung_funktion(werte):  #Funktion definieren
    x1= werte[0] #Indeces der Liste Werte angeben, Start immer bei 0
    y1= werte[1]
    x2= werte[2]
    y2= werte[3]
    
    delta_x = x2 - x1 #Differenzen definieren
    delta_y = y2 - y1
    
    if (delta_x == 0):
        print("Die Steigung ist nicht definiert")
    else:
        steigung= delta_y / delta_x
        return steigung # um den Wert auszugeben

print(steigung_funktion(werte = [4, 4, 8, 4])) # Werte eingeben
