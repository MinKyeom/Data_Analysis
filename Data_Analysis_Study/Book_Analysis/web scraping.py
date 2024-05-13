"""
출처: yes24
활용 출처:https://www.yes24.com/Product/Goods/126284479
"""

import requests
"""
https://www.yes24.com/Product/Goods/126284479
"""
isbn=126284479

url="https://www.yes24.com/Product/Goods/{}"

r=requests.get(url.format(isbn))

print(r.text)

### html ### html에서 데이터 추출하기

from bs4 import BeautifulSoup

soup=BeautifulSoup(r.text,"html.parser")
prd_link=soup.find("h2", attrs={"class":"gd_name"})

print(prd_link)
