import requests
from bs4 import BeautifulSoup
'''
naver 뉴스에서 검색어를 검색하여 나온 기사의 제목과 링크를 크롤링
'''
search_what = "광주 인공지능"
start_num = 11  # 11부터 시작
URL = f"https://search.naver.com/search.naver?&where=news&query={search_what}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start={str(start_num)}&refresh_start=0"

res = requests.get(URL)
print(res)

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

result = soup.select("ul.type01 > li > dl > dt > a")
# print(result)

for news in result:
    title = news.text
    link = news.attrs['href']
    
    print(title)
    print(link)
