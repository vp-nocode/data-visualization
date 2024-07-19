'''
1. Создать гистограмму для случайных данных, сгенерированных с помощью функции numpy.random.normal`.
# Параметры нормального распределения
mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


mean = 0
std_dev = 1
num_samples = 1000
data = np.random.normal(mean, std_dev, num_samples)

sns.histplot(data, kde=True, bins=20, edgecolor='black')
plt.title('Normal distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
