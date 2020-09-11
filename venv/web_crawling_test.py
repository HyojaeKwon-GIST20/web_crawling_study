from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import urllib.request

base_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plus_url = input('검색하고 싶은 단어를 넣어 주셈')

url = base_url+quote_plus(plus_url)

html=urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

print(url)
image=soup.find_all(class_='_img')


n=1
for i in image:
    img_url=i['data-source']
    print(img_url)
    urllib.request.urlretrieve(img_url,'C:/Users/khj01/Desktop/hi/'+str(n)+'.jpg')
    n+=1
