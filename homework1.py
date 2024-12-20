import matplotlib.pyplot as plt

def spar_funktion(AK, SR, i, lz):
    kapital = AK # Variable erstellen, damit es nacher noch geändert werden kann
    gesamt_kapital = [] # leere Liste in der Ergebnisse der Berechnung gespeichert werden soll
    
    for k in range(1, lz+1):
        kapital = SR + kapital * (1+i) #Verzinsed addieren je runde
        gesamt_kapital.append(round(kapital, 2)) # berechnetes Kapital in gesamt_kapital speichern, gerundet in 2 Nachkommastellen, noch in Funktion aber nicht mehr in for schleife
        
    return gesamt_kapital     # was zurückgegeben werden soll, die liste 

#print(spar_funktion(AK= 10000,
                  #  SR= 1000,
                  #  i= 0.01,
                 #   lz = 10))

sparplan = spar_funktion(AK= 10000, SR= 1000, i= 0.01, lz = 10)

plt.bar(range(1,11), sparplan )   # Jahre 1-10, und vorherige werte erst in Variable sparplan speichern