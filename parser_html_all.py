from bs4 import BeautifulSoup
import csv
import os


def get_url_models(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='ListingItem__description')
        url = []
        for item in items_divs:
            url.append(item.find('h3').find('a').get('href'))
        # print('is done--1')
        return url


def get_model(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('a', class_='Link ListingItemTitle__link')
        model = []
        for item in items_divs:
            model.append(item.text)
        # print('is done--2')
        return model


def get_year(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='ListingItem__yearBlock')
        year = []
        for item in items_divs:
            year.append(item.text)
        # print('is done--3')
        return year


def get_price(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='ListingItemPrice__content')
        price = []
        for item in items_divs:
            price.append(item.get_text().replace(u'\xa0', u' '))
        # print('is done--4')
        return price


def get_km(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='ListingItem__kmAge')
        km = []
        for item in items_divs:
            km.append(item.get_text().replace(u'\xa0', u' '))
        # print('is done--5')
        return km


def get_col(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        items_divs = soup.find_all('div', class_='ListingItemTechSummaryDesktop__cell')
        description = []
        for item in items_divs:
            it = item.get_text('|', strip=True).strip()
            description.append(it)
        # print(len(description))

        # удаление опций
        for j in description:
            j.replace('/', '/n')
            if 'опци' in j:
                description.remove(j)
        # print(len(description))

        # print('is done--6')
        return description

cities = [
    'moskovskaya_oblast',
    'moskva',
    'sankt-peterburg',
    'chelyabinsk',
    'omsk',
    'tomskaya_oblast',
    'vladivostok',
    'primorskiy_kray',
    'vladimir',
    'volgograd',
    'voronezh',
    'ekaterinburg',
    'ivanovo',
    'kazan',
    'kaluga'
    'kostroma',
    'krasnoyarsk',
    'krasnodar',
    'nizhniy_novgorod',
    'omsk',
    'perm',
    'rostov-na-donu',
    'samara',
    'saratov',
    'tver',
    'tula',
    'ufa',
    'yaroslavl'
]
with open(f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\all_cars.csv', 'w',
          encoding='utf-32') as f:
    for city in cities:
        for mark in ['BMW', 'Chery', 'Chevrolet', 'Citroen', 'Daewoo', 'Daihatsu', 'EXEED',
                  'Ford', 'Honda', 'Hyundai', 'Infiniti', 'Kia', 'Land Rover', 'Lexus',
                  'Lifan', 'Mazda', 'Mercedes-Benz', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Porsche',
                  'Renault', 'Skoda', 'SsangYong', 'Subaru', 'Suzuki', 'Toyota', 'Volkswagen', 'Volvo', 'ГАЗ',
                  'УАЗ', 'Audi', 'LADA (ВАЗ)']:

            #C:\Users\user\PycharmProjects\pythonProject2\CARS\Mercedes-Benz

                name_col = ['url', 'model', 'price', 'year', 'km', 'cost', 'descrip', 'city', 'mark']
                write = csv.writer(f)
                write.writerow(name_col)
                for i in range(1, 73, 1):
                    if os.path.exists(f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html'):
                        #print(f'Page {i}')
                        url = get_url_models(
                            f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        price = get_price(
                            f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        year = get_year(
                            f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        model = get_model(
                            f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        km = get_km(f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        descrip = get_col(
                            f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark}\\auto_marka_{i}.html')
                        # print(f'length url: {len(url)}')
                        # print(f'length descrip: {len(descrip)}')
                        for j in range(len(url) - 1):
                            # t = []
                            # t.append([url[j], model[j], price[j], year[j], km[j], descrip[j*5:(j+1)*5]])
                            if j == 0:
                                write.writerow([url[j], model[j], price[j], year[j], km[j], descrip[0], descrip[1:5], city, mark])

                            elif j != len(url) - 1:
                                write.writerow(
                                    [url[j], model[j], price[j], year[j], km[j], descrip[j * 5],
                                     descrip[j * 5 + 1: (j + 1) * 5], city, mark])
                            elif j == len(url) - 1:
                                write.writerow(
                                    [url[j], model[j], price[j], year[j], km[j], descrip[j * 5],
                                     descrip[j * 5 + 1: len(url)], city, mark])
                       # print(f'{i} page is done')

           # print(f'{j} marka is done')

