#3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# Функция для парсинга цен на диваны
def parse_divan_prices(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите все элементы с ценами
    prices = []
    for price_tag in soup.find_all('span', class_='price'):
        price = price_tag.text.strip().replace('₽', '').replace(' ', '')
        prices.append(float(price))

    return prices


# URL сайта для парсинга
url = 'https://divan.ru/'
prices = parse_divan_prices(url)

# Сохранение цен в CSV файл
df = pd.DataFrame(prices, columns=['Price'])
df.to_csv('divan_prices.csv', index=False)

# Обработка данных
average_price = df['Price'].mean()
print(f'Средняя цена диванов: {average_price:.2f} ₽')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Price'], bins=20, color='blue', alpha=0.7)
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (₽)')
plt.ylabel('Количество')
plt.grid(axis='y', alpha=0.75)
plt.show()

