import numpy as np 
import math
from Lab_3_main_1 import ge as g

h = 100
a = math.pi/3
b = 30

V = math.sqrt(((g * h)*(math.tan(b)**2))/(2 * (math.cos(a)**2)) * ((1 - math.tan(b)) * math.tan(a)))
print(float(V))



