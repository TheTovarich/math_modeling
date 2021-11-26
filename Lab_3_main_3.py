import numpy as np 
from Lab_3_main_1 import ge as g

t = np.arange(0, 5, 1)

x0 = 0
y0 = 0
x1 = 1
y1 = 4

X = x0 + x1 * t
Y = y0 + y1 * t - (g * t**2)/2

print(X)
print(Y)
ptint(t)


