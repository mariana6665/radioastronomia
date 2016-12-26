import numpy as np
import matplotlib.pyplot as plt

"""
Test Hot-Cold
"""

W_hot = 0.09
W_cold = 0.057

y = W_hot/W_cold

T_hot = 292 #temperatura ambiente en Kelvin
T_cold = 77 #temperatura Nitrogeno liquido en Kelvin

T_R = (T_hot - y*T_cold)/(y-1)

#print T_R


"""
Antenna Dipping
"""

alpha = [23.5, 16.6, 12.84, 10.48, 8.85, 7.66, 6.76, 6.04, 5.47, 4.99]
z = []
for i in range(10):
    n = (90 - alpha[i])*np.pi/180
    z = z + [n]
    i = i + 1
W_sky  = [0.077, 0.0815, 0.084, 0.0859, 0.0867, 0.0877, 0.0879, 0.0883, 0.0884, 0.0886]

dW = []
for i in range(10):
    n = 0.09 - W_sky[i]
    dW = dW + [n]
    i = i + 1

tau = np.log(dW)*np.cos(z)

ln_dW = np.log(dW)
sec_z = 1/np.cos(z)

j = 0
#para sacar la pendiente (tau)
for i in range(10):
    j = j + tau[i]
    i = i + 1
tauu = j/10.0

print j
print tauu
print tau
"""
fig=plt.figure()
plt.plot(sec_z,ln_dW, '-o')
plt.title('$Sec(z)$ $vs$ $ln( \Delta \omega )$')
plt.xlabel('$sec(z)$')
plt.ylabel('$ln( \Delta \omega)$')
plt.savefig('TAU.png')
plt.show()
"""


"""
Pointing
"""

A = np.loadtxt("sdf_13_13", skiprows = 108, usecols = [1])
max_1 = np.max(A)
ras_1 = 18.979591
dels_1 = -36.930832

B = np.loadtxt("sdf_16_16", skiprows = 108, usecols = [1])
max_2 = np.max(B)
ras_2 = 18.958742
dels_2 = -36.930832

C = np.loadtxt("sdf_17_17", skiprows = 108, usecols = [1])
max_3 = np.max(C)
ras_3 = 18.969166
dels_3 = -36.930832

D = np.loadtxt("sdf_20_20", skiprows = 108, usecols = [1])
max_4 = np.max(D)
ras_4 = 18.969166
dels_4 = -36.805832

E = np.loadtxt("sdf_24_24", skiprows = 108, usecols = [1])
max_5 = np.max(E)
ras_5 = 18.969166
dels_5 = -37.055832

"""
print "Temperaturas maximas"
print max_1
print max_2
print max_3
print max_4
print max_5
"""
