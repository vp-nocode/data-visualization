'''
3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
обработать данные, найти среднюю цену и вывести ее,
а также сделать гистограмму цен на диваны
'''

import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import matplotlib.pyplot as plt


url = 'https://www.divan.ru/category/divany'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
price_elements = soup.find_all('span', class_='ui-LD-ZU KIkOH')

# Извлекаем цены и записываем их в список
prices = []
for price_element in price_elements:
    print(price_element.get_text(strip=True))
    price_text = price_element.get_text(strip=True).replace(' ', '').replace('руб.', '')  # Убираем пробелы и символ рубля
    if price_text.isdigit():  # Проверяем, что это число
        prices.append(int(price_text))
print('data extracted')

# Записываем цены в CSV-файл
outfile = 'sofa_prices.csv'
with open(outfile, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Price'])
    for price in prices:
        csvwriter.writerow([price])
print(f'data stored in {outfile}')

# Вычисляем среднюю цену
average_price = np.mean(prices)
print(f'\nAverage price of a sofa: {average_price:,.2f} ₽')

# Строим гистограмму цен
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Histogram of Sofa Prices')
plt.xlabel('Price (₽)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
