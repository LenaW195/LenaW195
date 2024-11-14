
from math import log10
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

x_log10 = [log10(k) for k in x]
# Output ist eine Liste

x_log10_array = np.log10(x)  # funktion geht auf jedes einzelne Element der Liste x
# Output ist eine numpy array


