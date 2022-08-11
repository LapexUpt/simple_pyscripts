import requests
from bs4 import BeautifulSoup


url = 'https://pogoda.vtomske.ru/'
response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
temp = bs.find('div', class_='deg')

print('Температура воздуха в Томске сейчас:', temp.text)