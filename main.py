#imports
import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Constants and variables
mainURL = 'https://wallpaperscraft.ru'
pageLink = 'https://wallpaperscraft.ru/catalog/anime/1920x1080/page1'


response = requests.get(pageLink, headers={'User-Agent' : UserAgent().chrome})
html = response.content
soup = BeautifulSoup(html,'html.parser')
bufObj = soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['wallpapers__link'])
arrayOfAddURL = [link.attrs['href'] for link in bufObj]
print (arrayOfAddURL[:15])