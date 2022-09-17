import random

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from multiprocessing import Pool
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
# options
options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent= Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.1027 Yowser/2.5 Safari/537.36')

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")


# driver = webdriver.Chrome(executable_path='C:\\Users\\user\\PycharmProjects\\pythonProject2\\Selenium\\Chromedriver\\chromedriver.exe',
#                           options=options)

def get_html(a):
    # assert b <=34, 'Exceeded the maximum number of pages'
    # assert a >= 0, 'a should be positive'
    # assert a < b, 'b greater than a'

    try:
        for city in cities:
            for j in range(a, a + 5):
                driver = webdriver.Chrome(
                    executable_path=r'C:\Users\user\PycharmProjects\pythonProject2\Selenium\Chromedriver\chromedriver.exe',
                    options=options)
                driver.get(f'https://auto.ru/{city}/')
                #driver.maximize_window()
                time.sleep(random.randint(10, 15))
                # - капча, которая кликабельная
                driver.find_element(by=By.CLASS_NAME, value='CheckboxCaptcha-Anchor').click()
                time.sleep(random.randint(10, 15))
                mark = driver.find_elements(by=By.CLASS_NAME, value='IndexMarks__item-name')  # лист с марками
                # n = len(mark)
                # print(f'Number of marks is {n}')
                time.sleep(random.randint(10, 15))
                newpath = f'C:\\Users\\user\\PycharmProjects\\pythonProject2\\CARS\\{city}\\{mark[j].text}'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                time.sleep(5)
                #print('i here')
                mark[j].click()
                time.sleep(random.randint(10, 15))
                #print('is done')
                # переключение на страницу
                flag = 0
                for i in range(70, 100):
                    if flag ==3:
                        break
                    time.sleep(5)
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
                    if os.path.exists(newpath + f'\\auto_marka_{i}.html'):
                        #print('aaaa')
                        continue
                    if len(driver.find_elements(by=By.LINK_TEXT, value=f'{i}')) == 0:
                        print('------')
                        flag += 1
                        continue
                        # driver.get('https://auto.ru/')
                        # driver.maximize_window()
                        # time.sleep(5)
                        # driver.find_element(by=By.CLASS_NAME, value='CheckboxCaptcha-Anchor').click()
                    else:
                        driver.find_elements(by=By.LINK_TEXT, value=f'{i}')[0].click()
                        print(f'i am complete {i} page')
                        time.sleep(7)
                        with open(newpath + f'\\auto_marka_{i}.html', 'w', encoding='utf-8') as file:
                            file.write(driver.page_source)
                        time.sleep(7)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


# a = [0, 5]
a = [0, 5, 10, 15, 20, 25, 30]
if __name__ == '__main__':
    p = Pool(processes=7)
    p.map(get_html, a)
