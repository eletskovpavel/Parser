#imports
import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Constants and variables
mainURL = 'https://wallpaperscraft.ru'
pageLink = 'https://wallpaperscraft.ru/catalog/anime/1920x1080/page1'

def getURLsFromOnePage(page): #Данная функция принимает url страницы, и находит все url, которые ведут к страницам изображений, возвращает массив добавочных URL
    response = requests.get(page, headers={'User-Agent' : UserAgent().chrome})
    html = response.content
    soup = BeautifulSoup(html,'html.parser')
    bufObj = soup.findAll(lambda tag: tag.name == 'a' and tag.get('class') == ['wallpapers__link'])
    arrayOfAddURL = [link.attrs['href'] for link in bufObj]
    return arrayOfAddURL

def createFullURLs(arrayOfShortURLs): #create array of Full URLs, pages where img located
    bufList = []
    for element in arrayOfShortURLs:
        bufList.append(mainURL+element)
    arrayOfFullURLs = bufList
    return arrayOfFullURLs

def getDownloadURL(url): #gets URL for download image 
    newResponse = requests.get(url, headers={'User-Agent' : UserAgent().chrome})
    html = newResponse.content
    soup = BeautifulSoup(html,'html.parser')
    bufObj = soup.find(lambda tag: tag.name == 'a' and tag.get('class') == ['JS-Popup'])
    url = bufObj.attrs['href']
    return url

def clearingURL(elmentOfArray): #delete ', [ and ] from element of URL's array
    string = str(elmentOfArray)
    string = string.replace("[","")
    string = string.replace("]","")
    string = string.replace("'","")
    return string


def saveImage (link,name): # saving image in current folder 
    imgData = requests.get(link).content
    with open (name + '.jpg','wb') as handler:
        handler.write(imgData)

listOfShortURLs = getURLsFromOnePage(pageLink)
listOfFullURLs = createFullURLs(listOfShortURLs)
string = clearingURL(listOfFullURLs[:1])
imgURL = getDownloadURL(string)
saveImage(imgURL, 'kek')

