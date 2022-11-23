from selenium import webdriver
from bs4 import BeautifulSoup
import time

try:
    options = webdriver.ChromeOptions()
    options.binary_location = 'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'

    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    url = 'https://www.bbc.com/'
    driver.get(url)

    time.sleep(2)
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    alla = soup.find_all('a')

    links = []
    for link in alla:
        link = link.get('href')
        if url + 'news/' in link:
            links.append(link)

    links = list(dict.fromkeys(links))
    print(len(links))

    with open('links.txt', 'w', encoding='utf-8') as file:
        for link in links:
            file.write(f'{link}\n')
except Exception as ex:
    print(ex)
finally:
    driver.stop_client()
    driver.close()
    driver.quit()