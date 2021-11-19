np.arange(start, stop, step)

import numpy as np

a = range(0, 5, 1) #будет ошибка
print(a)

b = np.arange(0, 5, 0.1)
print(b)

d = np.linespace(0, 5, 10)
print(d)


