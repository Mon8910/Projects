#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests 
import csv


# In[2]:


website=requests.get("https://www.imdb.com/chart/top/").text
website


# In[4]:


soup=BeautifulSoup(website,'lxml')
print(soup)


# In[14]:


csvfile=open("scrape7.csv",'w',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow(['movies','year','rating'])


# In[32]:


mov=soup.find_all('div','article')
mov


# In[109]:


movies=soup.find('tbody',class_='lister-list').find_all('tr')
print(len(movies))


# In[128]:


for i in movies :
    name=i.find('td',class_='titleColumn').a.text
    print(name)
    date=i.find('td',class_='titleColumn').span.text.strip('( )')
    print(date)
    number=i.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    print(number)
    rate=i.find('td',class_='ratingColumn imdbRating').strong.text
    print(rate)


# In[131]:


csvfile=open('scrap9.csv','w',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow(['number','name','date','rating'])
for i in movies :
    name=i.find('td',class_='titleColumn').a.text
    print(name)
    date=i.find('td',class_='titleColumn').span.text.strip('( )')
    print(date)
    number=i.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
    print(number)
    rate=i.find('td',class_='ratingColumn imdbRating').strong.text
    print(rate)
    writer.writerow([number,name,date,rate])
csvfile.close()


# In[ ]:




