#!/usr/bin/env python
# coding: utf-8

# ## 비즈워치 뉴스 헤드라인 -> 표로 만들기 

# (방법1) 리스트를 만들어서 데이터 프레임으로 전환
# (방법2) 시리즈로 데이터 프레임 만들기

# 비즈워치
# https://media.naver.com/press/648
# 
# 코드를 보기 좋게 
# https://beautifier.io/?without-codemirror

# from bs4 import BeautifulSoup
# 
# from urllib.request import urlopen
# 
# import pandas as pd
# 
# import json as json

# In[70]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import json as json


# ! pip install selenium
# 
# from selenium import webdriver

# In[71]:


get_ipython().system(' pip install selenium')
from selenium import webdriver


# * 웹 드라이버 불러오는 코드 수정버전:
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# driver=webdriver.Chrome(options=Options(), service=Service('C:/Users/thkim/Downloads/chromedriver_win32'))
# 
# * C:\Users\user\Documents\je-download\chromedriver_win32
# driver = webdriver.Chrome('C:/Users/user/Documents/je-download/chromedriver_win32')

# In[72]:


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

# In[73]:


html = driver.get('https://media.naver.com/press/648')
page = driver.page_source
bs_obj = BeautifulSoup(page, 'html.parser')

article_list = []
article_list = bs_obj.find_all('li', {'class': 'press_news_item'})
article_list


# (방법 1) list로 만들어 pd.DataFrame()으로 표 전환 

#  <span class="press_news_text">
#  <strong>'고만고만하면 도태'…멤버십 '옥석 가리기' 시작됐다</strong>
#  <span class="press_news_datetime">06월 14일 07:51</span

# In[78]:


news_title_list = []
for i in article_list:
    news_title_list.append(i.find('strong').text.replace('\n',''))
        
news_title_list        


# In[103]:


# <span class="press_news_text">
# <strong>'고만고만하면 도태'…멤버십 '옥석 가리기' 시작됐다</strong>
# <span class="press_news_datetime">06월 14일 07:51</span>
# date 

news_date_list = []
# for i in bs_obj.find_all('span', {'class':'press_news_datetime'}):
for i in bs_obj.find_all('span',{'class': 'press_news_datetime'}):
    print(i.text)
    news_date_list.append(i.text)

print('Length of the list -> ',len(news_date_list))
news_date_list


# In[34]:


news_link_list = []
for i in article_list:
    news_link_list.append(i.select('a')[0].get('href'))
        
news_link_list


# In[ ]:





# In[76]:


# 빈 데이터 프레임 만들기

df = pd.DataFrame()
df


# In[83]:


# 리스트를 만들고 이를 데이터 프레임으로 전환 

news_headline_list = []
news_link_list = []

for i in article_list:
    news_headline_list.append(i.select('strong')[0].text.replace('\n',''))
    news_link_list.append(i.select('a')[0].get('href'))
    
df = pd.DataFrame({'head line':news_headline_list, 'news link':news_link_list})
df    


# (방법2) 시리즈로 데이터 프레임 만들기 

# #열 헤더 리스트를 시리즈로 변환
# header = ['제목','미리보기','링크']
# row1 = pd.Series(header)
# 
# #빈 데이터 프레임에 열 헤더 설정
# df = pd.DataFrame(columns=row1)
# 
# #시리즈에 열 헤더 붙일때 사용하기 위해서 열 헤더 따로 빼놓기
# col = df.columns
# 

# In[89]:


header = ['headline', 'link']
row1 = pd.Series(header)
df = pd.DataFrame(columns = row1)
col = df.columns


# arr = []
# for article in bs_obj.find_all("div", {"class":"sh_text"}):
#     row = pd.Series([article.select('a')[0].text,article.select_one("div.sh_text_lede").text,
#                     article.select('a')[0].get('href')], index=col)
#     df = df.append(row, ignore_index=True)
# 

# In[90]:


# 앞에서 만든 df 비우기

df.drop(df.index, inplace=True)
df


# In[91]:


arr = []

for article in bs_obj.find_all('li', {'class': 'press_news_item'}):
    #print(article.find("strong").text)
    # row = pd.Series([article.find("strong").text, article.select_one('a').get('href')], index = col)
    dataframe1 = df.append(row, ignore_index = True)
    row = pd.Series([article.find('strong').text.replace('\n',''), article.select_one('a').get('href')], index = col)
    df = df.append(row, ignore_index = True)
                               
df


# In[ ]:


# fin

