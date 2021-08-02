import pandas as pd
import requests
from bs4 import BeautifulSoup
def extract(page):
    url = f'https://www.lybrate.com/panipat/treatment-for-acne-pimples?lpt=PS-HF'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    return soup
def tranform(soup):
    divs = soup.find_all('div', class_ = 'grid__col-15 lybPad-top')
    for item in divs:
        Name= item.find('a').text.strip()
        degree = item.find('div', class_ = "lybEllipsis ly-doctor__degree grid__col-20").text.strip()
        speciality =item.find('div',class_ = "lybText--dark lybText--ellipsis").text.strip()
        clinicName  =item.find('div',class_ ="lybText--dark lybText--ellipsis").text.strip()
        address= item.find('span',class_  ="lybGrey").text.strip()
        
        doc ={
            'Name' :Name,
            'degree' :degree,
            'speciality':speciality,
            'clinicName':clinicName,
            'address' : address
        }
        doclist.append(doc)      
    return
doclist = []
for i in range(10):
    print("successful",{i})
    c = extract(0)
    tranform(c)
df = pd.DataFrame(doclist)
print(df.head)
df.to_csv('doclist')
print(df)