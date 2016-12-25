import numpy as np

#Test Hot-Cold

W_hot = 0.09
W_cold = 0.057

y = W_hot/W_cold

T_hot = 292 #temperatura ambiente en Kelvin
T_cold = 77 #temperatura Nitrogeno liquido en Kelvin

T_R = (T_hot - y*T_cold)/(y-1)

#print T_R

#Antenna Dipping


alpha = [23.5, 16.6, 12.84, 10.48, 8.85, 7.66, 6.76, 6.04, 5.47, 4.99, W_hot]
z = []
for i in range(11):
    n = (90 - alpha[i])*np.pi/180
    z = z + [n]
    i = i + 1
W_sky  = [0.077, 0.0815, 0.084, 0.0859, 0.0867, 0.0877, 0.0879, 0.0883, 0.0884, 0.0886, 0.09]

dW = []
for i in range(11):
    n = 0.09 - W_sky[i]
    dW = dW + [n]
    i = i + 1

tau = np.log(dW)*np.cos(z)
