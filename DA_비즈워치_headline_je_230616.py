#!/usr/bin/env python
# coding: utf-8

# 비즈워치
# https://media.naver.com/press/648
# 
# 코드를 보기 좋게 
# https://beautifier.io/?without-codemirror

# from bs4 import BeautifulSoup\n
# from urllib.request import urlopen\n
# import pandas as pd\n
# import json as json

# In[7]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import json as json


# ! pip install selenium
# 
# from selenium import webdriver

# In[8]:


get_ipython().system(' pip install selenium')
from selenium import webdriver


# * 웹 드라이버 불러오는 코드 수정버전:
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# driver=webdriver.Chrome(options=Options(), service=Service('C:/Users/thkim/Downloads/chromedriver_win32'))
# 
# * C:\Users\user\Documents\je-download\chromedriver_win32
# driver = webdriver.Chrome('C:/Users/user/Documents/je-download/chromedriver_win32')

# In[9]:


# 웹 드라이버 불러오는 코드 수정버전:
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(options = Options(), service = Service('C:/Users/user/Documents/je-download/chromedriver_win32'))


# html = driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101')
# page = driver.page_source
# bs_obj =  BeautifulSoup(page,'html.parser')
# 
# article_list = []
# article_list = bs_obj.find_all("li", {'class':'sh_item _cluster_content'})
# 
# article_list

# In[10]:


html = driver.get('https://media.naver.com/press/648')
page = driver.page_source
bs_obj = BeautifulSoup(page, 'html.parser')

article_list = []
article_list = bs_obj.find_all('li', {'class': 'press_news_item'})
article_list


# In[25]:


news_title_list = []
for i in article_list:
    news_title_list.append(i.text.replace('\n',''))
        
news_title_list        


# In[34]:


news_link_list = []
for i in article_list:
    news_link_list.append(i.select('a')[0].get('href'))
        
news_link_list


# In[40]:


news_headline_list = []
news_link_list = []

for i in article_list:
    news_headline_list.append(i.text.replace('\n',''))
    news_link_list.append(i.select('a')[0].get('href'))
    
df = pd.DataFrame({'head line':news_headline_list, 'news link':news_link_list})
df    


# In[ ]:


# fin

