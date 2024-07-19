# Извлечение цен с учетом пагинации

import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import matplotlib.pyplot as plt


BASE_URL = 'https://www.divan.ru'
SOFAS_URL = f'{BASE_URL}/category/divany-i-kresla/page-'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_prices_from_page(page_number):
    url = SOFAS_URL + str(page_number)
    print(f'Processing {url}')
    try:
        response = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=10)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        price_elements = soup.find_all('span', class_='ui-LD-ZU KIkOH')

        prices = []
        for elem in price_elements:
            try:
                price_text = elem.get_text(strip=True).replace(' ', '').replace('руб.', '')
                if price_text.isdigit():
                    prices.append(int(price_text))

            except ValueError:
                continue

        return prices

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []


def parse_all_pages():
    all_prices = []
    page_number = 1

    while True:
        prices = get_prices_from_page(page_number)
        if not prices:
            break
        all_prices.extend(prices)
        print(f'{page_number} page processed')
        page_number += 1

    return all_prices


def save_to_csv(prices, filename='sofa_prices.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])
        for price in prices:
            writer.writerow([price])


def calculate_average(prices):
    return np.mean(prices)


def plot_histogram(prices, bins=20):
    plt.hist(prices, bins=bins, edgecolor='black')
    plt.title('Histogram of Sofa Prices')
    plt.xlabel('Price (₽)')
    plt.ylabel('Frequency')
    plt.show()


prices = parse_all_pages()
if not prices:
    print("Failed to extract price from site.")

save_to_csv(prices)

average_price = calculate_average(prices)
print(f'Average price of a sofa: {average_price:.2f} ₽')

plot_histogram(prices)
