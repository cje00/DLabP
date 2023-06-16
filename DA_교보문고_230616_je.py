#!/usr/bin/env python
# coding: utf-8

# ### 교보문고 추천 도서 

# In[ ]:


교보문고 https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=

코드를 보기 좋게 https://beautifier.io/?without-codemirror


# In[1]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import json as json


# In[4]:


get_ipython().system(' pip install selenium')
from selenium import webdriver


# 웹 드라이버 불러오는 코드 수정버전:
# - from selenium.webdriver.chrome.options import Options 
# - from selenium.webdriver.chrome.service import Service 
# - driver=webdriver.Chrome(options=Options(), service=Service('C:/Users/thkim/Downloads/chromedriver_win32'))
# 
# (fyi) C:\Users\user\Documents\je-download\chromedriver_win32
# 
# 이전 버전에서 사용하던 방식:
# - driver = webdriver.Chrome('C:/Users/user/Documents/je-download/chromedriver_win32')

# In[15]:


from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(options = Options(), service = Service('C:/Users/user/Documents/je-download/chromedriver_win32')) 


# In[16]:


html = driver.get("https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=")
page = driver.page_source
#html = urlopen("https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=")
bs_obj = BeautifulSoup(page, "html.parser")


# In[17]:


driver = webdriver.Chrome('C:/Users/user/Documents/je-download/chromedriver_win32')


# In[21]:


html = driver.get('https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=')
page = driver.page_source
bs_obj = BeautifulSoup(page, 'html.parser')


# In[26]:


df = pd.DataFrame()


# In[27]:


book_name = bs_obj.find_all('span', {'class':'prod_name'})
header = ['제목', '작가, 날짜', '가격', '도서 정보 자세히 보기']
row1 = pd.Series(header)

df = pd.DataFrame(columns = row1)
col = df.columns


# In[28]:


book_list = []

for books in bs_obj.find_all('li', {'class':'prod_item'}):
    title = books.find('span', {'class':'prod_name'}).text
    link = books.select('a')[0].get('href')
    author = books.find('span', {'class':'prod_author'}).text
    price = int(books.find('span', {'class':'val'}).text.replace(',',''))
    book_list.append([title, author, price, link])


for i in book_list:
    df = df.append(pd.Series(i, index = col), ignore_index = True)    
    
df


# In[ ]:


# fin

