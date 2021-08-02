import pandas as pd
import requests
import openpyxl
from bs4 import BeautifulSoup

website = requests.get('https://www.banggood.in/search/shoes.html?from=nav')
sp = BeautifulSoup(website.content,'html.parser')
#print(sp)
title= sp.find_all('a',class_ = 'title')
oldprice = sp.find_all('span',class_ = 'price-old-box')
sellprice= sp.find_all('span',class_= 'price-box')
review = sp.find_all('a',class_ = 'review')

titleloop= [titles.text for titles in title]
oldpriceloop = [oldpric.text for oldpric in oldprice]
old = []
for i in oldpriceloop:
    p = i.replace("\n"," ")
    old.append(p)
#print(old)
    
sellpriceloop = [sell.text for sell in sellprice]
sell =[]
for i in sellpriceloop:
    q = i.replace("\n"," ")
    sell.append(q)
#print(sell)
reviewloop = [revi.text for revi in review]
#decided column name here
data = {'Name of Itmes ': titleloop,
'Actual Price ': old,
'Discount Price ': sell,
'Review':reviewloop

}
#print(len(reviewloop))

df = pd.DataFrame(data,columns=['Name of Itmes ','Actual Price ','Discount Price ','Review'])
#print(df)
df.to_excel("shoeitem.xlsx")
