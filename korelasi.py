import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

X = np.array([28,20,21,23,17,25,22,19,27,25])
Y = np.array([21,24,27,22,26,24,23,25,21,22])
r = np.corrcoef(X, Y)

print('Ilham / 152017041')

print (r)