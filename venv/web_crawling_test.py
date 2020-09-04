from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plus_url = input('검색하고 싶은 단어를 넣어 주셈')

url = base_url+quote_plus(plus_url)

html =urlopen(url).read()



soup=BeautifulSoup(html,'html.parser')
title =soup.find_all(class ='sh_blog_title')


