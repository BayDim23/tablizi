#2. Построй диаграмму рассеяния для двух наборов случайных данных,
# сгенерированных с помощью функции `numpy.random.rand`.
#import numpy as np
#random_array = np.random.rand(5)  # массив из 5 случайных чисел
#print(random_array)

import matplotlib.pyplot as plt
import numpy
random_array = numpy.random.rand(5)  # массив из 5 случайных чисел
plt.plot(random_array)
plt.show()