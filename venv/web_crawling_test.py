from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import urllib.request
import os

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색하고 싶은 단어를 넣어 주셈')

url = base_url+quote_plus(plus_url)

html=urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
path='C:/Users/khj01/Desktop/'+plus_url
os.mkdir(path)
print(url)
image=soup.find_all(class_='_img')


n=1
for i in image:
    img_url=i['data-source']
    img_tit=i['alt']

    print(img_tit)
    print(img_url)
    print(" ")
    urllib.request.urlretrieve(img_url,'C:/Users/khj01/Desktop/'+plus_url+'/'+str(n)+'.jpg')
    n+=1
