import numpy as np

y= [2,3,8,4,10,1,9,5,1,0]

  # erst Wurzelfunktion y_std, dann was unter wurzel ist, n ist anzahl der elemenete der liste (daher len nutzen)
# dann kommt summe (np.sum) oder sum (weil es schon in python exiert), summieren der quadrierten Abweichung von y - 
# 
y_std = np.sqrt(1/len(y) * sum((y - np.mean(y)) **2) )