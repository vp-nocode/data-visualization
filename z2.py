'''
2. Построить диаграмму рассеяния для двух наборов случайных данных,
сгенерированных с помощью функции `numpy.random.rand
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.random.rand(100)
y = np.random.rand(100)

sns.scatterplot(x=x, y=y)
plt.title('Scatter plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
