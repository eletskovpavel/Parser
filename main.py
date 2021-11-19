#imports
import os
import time
import requests
import urllib.request
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Constants and variables
mainURL = 'https://wallpaperscraft.ru'
pageLink = 'https://wallpaperscraft.ru/catalog/anime/1920x1080/page'

def getURLsFromOnePage(page): #gets shorts url from page
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


def saveImage (link,name): # saving image in current folder with ur name
    imgData = requests.get(link, headers={'User-Agent' : UserAgent().chrome}).content
    with open (name + '.jpg','wb') as handler:
        handler.write(imgData)



def saveAllImagesFromOnePage (page): #function that contains all functions
    arrayOfShortURLs = getURLsFromOnePage(page)
    arrayOfFullURLs = createFullURLs(arrayOfShortURLs)
    for i in range(0,len(arrayOfFullURLs)):
        try:
            clearURL = clearingURL(arrayOfFullURLs[i])
            downloadURL = getDownloadURL(clearURL)
            saveImage(downloadURL,str(i+1))
            print ('image ' + str(i+1)+ ' downloaded successfully!')
        except:
            print('image ' + downloadURL + ' not downloaded!')
            continue

def saveAllImgInCategory (link):
    counter = 1
    while True:
        try:
            os.chdir("D:\PythonImgDownload")
            os.mkdir(str(counter))
            os.chdir("D:\PythonImgDownload"+'\\'+str(counter))
            saveAllImagesFromOnePage(link + str(counter))
            counter += 1
        except:
            print ("All done")
            os.rmdir("D:\PythonImgDownload"+'\\'+str(counter))

saveAllImgInCategory(pageLink)
