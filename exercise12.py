import numpy as np

M= np.array([3,2,1,4]).reshape(2,2)

M_inv = np.linalg.inv(M)  # Funktion M 

 # jetzt testen
I = np.matmul(M_inv, M)   # speichern als I (Inverse von M)

A = np.array([7, 5, -3, 3, -5,2,5,3,-7]).reshape(3,3)

r= np.array([16, -8, 0]).reshape(3,1)  # jetzt Vektor von Ergebnis, um einen Vektor mit 2 Dimensionsne zu bekommen 
#braucht man ein zweites reshape

A_inv = np.linalg.inv(A) # inverse von A ist A hoch -1

b= np.matmul(A_inv, r)