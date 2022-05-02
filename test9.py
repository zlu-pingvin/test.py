# import requests
# r = requests.get("https://tp-back.starlight.digital/ua/serials")
# response = r.json()
# for channel in response['channels']:
#     print("\n{}".format(channel['title']))
#     for serial in response['items']:
#         if channel['channelSlug'] in serial['channelSlug']:
#             print(serial['name'])
# print(r.text)


# array = ['white', 'red', 'yellow']
# test_dict = {'cat': 'Vasya', 'dog': 'Zhuchka'}
# test_dict['cat']
#
# name = "Andrey"
# for letter in name:
#     print(letter)

# массивы
# кортежи
# именованные словари
# переменные

# import requests
# r = requests.get("https://kinogoo.zone/4547-pes-6-sezon.html")
# response = r.json()
# for channel in response['channels']:
#     print("\n{}".format(channel['title']))
#     for serial in response['items']:
#         if channel['channelSlug'] in serial['channelSlug']:
#             print(serial['name'])
# print(r.text)

# import requests
# r = requests.get("https://kinogoo.zone/4547-pes-6-sezon.html")
# response = r.json()
# for channel in response['channels']:
#     print("\n{}".format(channel['title']))
#     for serial in response['items']:
#         if channel['channelSlug'] in serial['channelSlug']:
#             print(serial['name'])
# for title in r['title']:
#     print(r)
# print(r.text)

# import requests, lxml  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from bs4 import BeautifulSoup
# url = "https://a.kinogoo.zone/4547-pes-6-sezon.html"
# response = requests.get(url)
#
# pes = BeautifulSoup(response.text, 'lxml')
# print(pes)

# requests.get('https://teleportal.ua/ua/serials/stb/kriposna/')
# response = requests.get('https://a.kinogoo.zone/4547-pes-6-sezon.html')
# print(response)

# url = 'https://kinogoo.zone/4547-pes-6-sezon.html'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
# r = requests.get(url, headers=headers)
# for i, each in enumerate(r.history, 1):
#     print(f'{i} {each.status_code} {each.url}')


# r = requests.get('https://a.kinogoo.zone/4547-pes-6-sezon.html')
# print(r.status_code)

# r = requests.get('https://kinogoo.zone/4547-pes-6-sezon.html')
# r.url = 'https://kinogoo.zone/4547-pes-6-sezon.html'
# response = r.json()
# for Response in r:
#     print(r)
# print(r.status_code)
# print(r.history)

# import requests
# r = requests.get('https://kinogoo.zone/4547-pes-6-sezon.html', allow_redirects=True)
# for response in r.history:
#     print(response.url, ' Нерабочий сайт')
# print(r)
# print(r.url, 'Сайт сейчас доступен для просмотра')

# import speedtest
#
# test = speedtest.Speedtest()
# download = round()test.download()
# upload = test.upload()
#
# print(f'Download speed: {(download/1024)/1024} Mb/s')
# print(f'Upload speed: {(upload/1024)/1024} Mb/s')

# import speedtest
#
# test = speedtest.Speedtest()
# download = test.download()
# upload = test.upload()
#
# dwn = round((download/1024)/1024, 2)
# upl = round((upload/1024)/1024, 2)
#
# print(f'Download speed: {dwn} Mb/s')
# print(f'Upload speed: {upl} Mb/s')

# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://rozetka.com.ua/consoles/c80020/producer=playstation/")
# response = r.json()
#
#
# pes = BeautifulSoup(response.text, 'lxml')
# print(pes)

# import requests, lxml
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('span', class_='goods-tile__title').text
# status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
# price = soup.find('span', class_='goods-tile__price-value').text
# print(title)
# print(price)
# print(status)

# import requests  # 1 товар
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('span', class_='goods-tile__title').text
# status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
# price = soup.find('span', class_='goods-tile__price-value').text
# print(title)
# print(price)
# print(status)
#
# import requests, lxml
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
#
# start = -1
# while start < 0:
#     title = soup.find( 'span', class_='goods-tile__title').text
#     status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
#     price = soup.find('span', class_='goods-tile__price-value').text
#     print(title)
#     print(price)
#     print(status)
#     start + 1

# import requests  # ps5
# from bs4 import BeautifulSoup
# url = ['https://rozetka.com.ua/sony_playstation_ps5_msm/p328158313/', 'https://rozetka.com.ua/sony_playstation_9398806_9863625_9321309_9809944/p319497217/', 'https://rozetka.com.ua/sony_playstation_9398806_9399902_9374107_9809944/p319129303/', 'https://rozetka.com.ua/sony_playstation_9398707_1103888_9809944_9399902/p319124671/', 'https://rozetka.com.ua/sony_playstation_9398707_9714798_9815396/p319122463/', 'https://rozetka.com.ua/sony_playstation_ps5_dms_nc/p328159375/', 'https://rozetka.com.ua/sony_playstation_9398707_9812623_9837022/p319114585/', 'https://rozetka.com.ua/sony_playstation_9398806_9387909_9809944/p319133506/', 'https://rozetka.com.ua/sony_playstation_9398707_9827290_9826729/p319123747/']
# for i in range(9):
#     n = url[i]
#     r = requests.get(n)
#     soup = BeautifulSoup(r.text, 'lxml')
#     title = soup.find('h1', class_='product__title').text
#     status = soup.find('p', class_='status-label status-label--blue ng-star-inserted').text
#     price = soup.find('p', class_='product-prices__big').text
#     print(n)
#     print(title)
#     print(price)
#     print(status)

# import requests
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# title1 = soup.findAll('span', class_='goods-tile__title')
# for i in title1:
#     title = soup.find('span', class_='goods-tile__title').text
#     print(title)
# status1 = soup.findAll('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted')
# # status = status1.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
# for j in status1:
#     status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
#     print(status)
# price = soup.find('span', class_='goods-tile__price-value').text
# # print(title)
# print(price)
# print(status)

# import requests  # 1 товар
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('span', class_='goods-tile__title').text
# status = soup.findAll('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted')
# price = soup.find('span', class_='goods-tile__price-value').text
# print(title)
# print(price)
# print(*status, sep='\n')


# import requests, lxml
# from bs4 import BeautifulSoup
# url = 'https://common-api.rozetka.com.ua/v2/locations/get-locality-info?front-type=xl&country=UA&lang=ru&id=1&r=0.9797852072072384'
# r = requests.get(url)
# response = r.json()
# soup = BeautifulSoup(r.text, 'lxml')
# print(soup)

# import requests, lxml  # IP
# from bs4 import BeautifulSoup
# url = 'https://2ip.ua/ua/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# ip = soup.find('div', class_='ip').text.strip()
#
# print(f'IP: {ip}')

# import requests, lxml  # IP
# from bs4 import BeautifulSoup
# url = 'https://whoer.net/ru'  # Сайт
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# ip = soup.find('div', class_='your-ip').text.strip()  # Тянем IP, выводим текст, убираем лишние пробелы
# loc = soup.find('span', class_='cont overdots').text.strip()  # Тянем страну, которой принадлежит IP, выводим текст, убираем лишние пробелы
#
# print(f'IP: {ip}')
# print(f'Страна: {loc}')
#
# import speedtest
#
# test = speedtest.Speedtest()
# download = test.download()
# upload = test.upload()
#
# dwn = round((download/1024)/1024, 2)
# upl = round((upload/1024)/1024, 2)
#
# print(f'Download speed: {dwn} Mb/s')
# print(f'Upload speed: {upl} Mb/s')

# import requests  # 1 товар
# from bs4 import BeautifulSoup
# url = 'https://rozetka.com.ua/consoles/c80020/producer=playstation/'
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'lxml')
# title = soup.find('span', class_='goods-tile__title').text
# status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
# price = soup.find('span', class_='goods-tile__price-value').text
# ps5all = soup.findAll('span', class_='goods-tile__title')+soup.findAll('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted')+soup.findAll('span', class_='goods-tile__price-value')
#
# data = []
#
# for ps in ps5all:
#     title = soup.find('span', class_='goods-tile__title').text
#     data.append(title)
#     status = soup.find('div', class_='goods-tile__availability goods-tile__availability--waiting_for_supply ng-star-inserted').text
#     data.append(status)
#     price = soup.find('span', class_='goods-tile__price-value').text
#     data.append(price)
#
#     data.append([title, status, price])
#
# for i in data:
#     print(*data)
#
# print(*data)
# print(title)
# print(price)
# print(status)
# print(ps5all)
#
# for i in data:
#     print(i)
#
# lines = 0
# for i in ps5all:
#     lines += 1
#     print('Line', lines, ' ', i)

