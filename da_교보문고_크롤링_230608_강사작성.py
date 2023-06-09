# -*- coding: utf-8 -*-
"""DA_교보문고 크롤링_230608_강사작성.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PkaFzF5efliuaEEy5zcAVpYlbhKD0-zs
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('C:/Users/thkim/Downloads/chromedriver_win32')
html = driver.get("https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=")
page = driver.page_source
#html = urlopen("https://product.kyobobook.co.kr/bestseller/online?period=001#?page=1&per=20&ymw=&period=001&saleCmdtClstCode=&dsplDvsnCode=000&dsplTrgtDvsnCode=001&saleCmdtDsplDvsnCode=")
bs_obj = BeautifulSoup(page, "html.parser")

book_name = bs_obj.find_all("span", {"class":"prod_name"})

header = ['제목', '작가, 날짜', '가격', '제품링크']

row1 = pd.Series(header)

df = pd.DataFrame(columns = row1)
col = df.columns



book_list=[]
for books in bs_obj.find_all("li",{"class":"prod_item"}):
    title = books.find("span", {"class": "prod_name"}).text
    link = books.select('a')[0].get('href')
    author = books.find("span", {"class": "prod_author"}).text
    price = int(books.find("span", {"class":"val"}).text.replace(',', ''))
    book_list.append([title, author, price, link])


for i in book_list:
    df=df.append(pd.Series(i, index=col), ignore_index=True)


df













