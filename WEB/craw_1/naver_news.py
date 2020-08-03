import requests
from bs4 import BeautifulSoup
import csv
'''
naver 뉴스에서 검색어를 검색하여 나온 기사의 제목과 링크를 크롤링
'''
soup_objects = []
for i in range(1, 102, 10):
    search_what = "광주 인공지능"
    start_num = i  # 1, 11, 21, ....
    URL = f"https://search.naver.com/search.naver?&where=news&query={search_what}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=32&start={str(start_num)}&refresh_start=0"

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")
    soup_objects.append(soup)
    
dict_data = []
for soup in soup_objects:
    result = soup.select("ul.type01 > li > dl > dt > a")
    for news in result:
        title = news.text
        link = news.attrs['href']

        news_data = {
            'title': title,
            'link': link
        }
        dict_data.append(news_data)

# dict -> csv Save
with open('./news_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'link'])
    writer.writeheader()
    for data in dict_data:
        writer.writerow(data)

