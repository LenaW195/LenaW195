
#While Schleife mit break bauen

a = 1
r = 0.5
s = 0
k = 0
limit = (a/ (1 - r)) # Grenze definieren
epsilon = 0.001   # 2te Variable die definiert wird

while True:  # immer richtig, läuft unendlich
    s += a * r**k
    k += 1
    print(s, end = " ")
    
   # if s == (a/(1-r)):  # das soll genau 2 werden und dann stoppen, "unsaubere lösung" python stoppt aber mathematisch nicht korrekt, da es nie 2 erreichen würde
 #       break


# elegantere  (oben zusätzliche Variablen definieren)

    if (limit - s) < epsilon:
        break
 