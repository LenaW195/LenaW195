
import matplotlib.pyplot as plt



#Werte definieren

r = 0.5
a = 1
n = 10

s_n = []  # leere Liste erstellen
summe = 0  # Anfangswert für die Summe definieren (damit nachher kummuliert werden kann)

for k in range(0, n):  #' Index ist hier k kann aber andere buchstabe oder wort sein muss nur konsequent sein
    summe += (a*(r**k))       # summieren mit Kummulator +=
    s_n.append(summe)   # methode append, dann wird summe reingepackt
    
print(s_n)
    
plt.plot(s_n)
    