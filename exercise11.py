import numpy as np

data = np.arange(1, 11)

#D= np.tile(data, 10)  # 2 D Array erstellen (was wiederholen, Anzahl der wiederholungen))

D= np.tile(data, 10). reshape(10, 10)

print(D.sum(axis = 0))

print(D.mean(axis=1)) #summieren und dann mittelwert der 2. Achse bilden (Achse in horizontaler Ebene)