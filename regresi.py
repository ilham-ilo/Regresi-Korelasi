#library-library yang dibutuhkan
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

#data untuk variable X untuk Kolom X dan Y untuk kolom Y
X_train = np.array([28,20,21,23,17,25,22,19,27,25])
y_train = np.array([21,24,27,22,26,24,23,25,21,22])
X_train = X_train.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)

#Create linear regression object
model_reg = LinearRegression()

#train the model using the training sets
model_reg.fit(X_train, y_train)

print('Ilham / 152017041')

print('Panjang X = {}'.format(len(X_train)))
print('Panjang Y = {}'.format(len(y_train)))

#regression coefficients
print('Koefisien = {}'.format(model_reg.coef_))
print('Konstanta ={} '.format(model_reg.intercept_))