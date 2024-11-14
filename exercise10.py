import numpy as np

M = np.eye(5, dtype="int")  # definieren der 2 D Funktion. funktion eye ist für identitäts-Matrix
M[0:2, 3:5] = 3   # ziel in obere rechte Ecke der Matrix 3 en bringen, [erste:2 reihe bzw. Zeile, 3te und: 5 exclusiv]]
M[3:5, 0:2] = 2