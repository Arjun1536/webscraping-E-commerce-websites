import requests
from bs4 import BeautifulSoup
import html5lib
url = "https://www.codewithharry.com"
#Get Html code
r = requests.get(url)
htmlcontent = r.content
#print(htmlcontent)
# Parse the html
#print(soup.prettify)
#Tree travesal 
#title =soup.title
#print(title)
para = soup.find_all('p')
#print(soup.find('p'),['class'])
#print(soup.find('p').get_text())
anch =soup.find_all('a')
#all = set()
#for i in anch:
    #all = 'http://codewithharry'+(i.get('href'))
    #print(all)
navbarsupported = soup.find('id = navbarSupportedContent')
for ele in navbarsupported.strings:
    print(ele)    