#!/usr/bin/env python
# coding: utf-8

# naver news
# https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101
# 
# code 보기 좋게 보여 주기
# https://beautifier.io/?without-codemirror

# In[2]:


get_ipython().system(' pip install selenium')
from selenium import webdriver


# In[ ]:


#  필요한 경우/ 새로운 버전 

# 웹 드라이버 불러오는 코드 수정버전:
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome(options=Options(), service=Service('C:/Users/thkim/Downloads/chromedriver_win32'))


# In[3]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
get_ipython().system(' pip install selenium')
from selenium import webdriver
import pandas as pd

# C:\Users\user\Documents\je-download\chromedriver_win32
driver = webdriver.Chrome('C:/Users/user/Documents/je-download/chromedriver_win32')

# url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
# html = driver.get(url)

html = driver.get('https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101')
page = driver.page_source
bs_obj =  BeautifulSoup(page,'html.parser')

article_list = []
article_list = bs_obj.find_all("li", {'class':'sh_item _cluster_content'})

article_list


# In[4]:


article_list[0]


# In[43]:


headlines = []

for headline in article_list:
    headline1 = headline.find('a',{'class':"sh_text_headline nclicks(cls_eco.clsart)"})
    headline2 = headline1.text.replace('<**>','')
    headlines.append(headline2)
    
headlines


# <참고용>
# 
# book_list=[]
# for books in bs_obj.find_all("li",{"class":"prod_item"}):
#     title = books.find("span", {"class": "prod_name"}).text
#     link = books.select('a')[0].get('href')
#     author = books.find("span", {"class": "prod_author"}).text
#     price = int(books.find("span", {"class":"val"}).text.replace(',', ''))
#     book_list.append([title, author, price, link])
#     
# for i in book_list:
#     df=df.append(pd.Series(i, index=col), ignore_index=True)
#    
# df

# In[44]:


len(headlines)


# In[9]:


news_links = []

for news_link in article_list:
    news_link1 = news_link.select('a')[0].get('href')                         
    news_links.append(news_link1)    

news_links


# In[21]:


len(news_links)


# In[46]:


article_view = []

for preview in article_list:
    preview1 = preview.find('div',{'class':"sh_text"}).text.replace('\n','')
    #preview2 = preview1[0].text
    article_view.append(preview1)

article_view


# In[47]:


len(article_view)


# In[39]:


previews = []

for preview in article_list:
    preview1 = preview.find('div',{'class':"sh_text_lede"}).text
    #preview2 = preview1[0].text
    previews.append(preview1)
    
previews


# In[40]:


len(preview)


# In[38]:


len(article_list)


# In[48]:


# data = {'headline': headlines, 'preview': preview, 'article link': news_links}
data = {'headline': headlines, 'preview': article_view, 'article link': news_links}
# data = {'headline': headlines, 'article link': news_links}


# In[49]:


df = pd.DataFrame(data)
df


# In[ ]:




