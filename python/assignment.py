import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https://www.lybrate.com/panipat/treatment-for-acne-pimples?lpt=PS-HF'
page  = requests.get(url)
#print(page)
page = page.content #class="ly-doctor__name grid__col-20 lybEllipsis"
soup = BeautifulSoup(page,'html.parser')
print(soup)
'''
results = soup.find_all('div', class_ ="grid__col-15 lybPad-top")
#print(results)
#print(soup.get_text())

for result in results:
    name = result.find('h2',class_ = "ly-doctor__name grid__col-20 lybEllipsis")
    speacility =result.find('div',class_ = "lybText--dark lybText--ellipsis")
    address = result.find('div', class_ ="lybGrey")
    
    print(f"postion: {name.text}")
    print(f"speciality: {speacility.text}")   
    print(f"address: {address.get}")
     
'''
