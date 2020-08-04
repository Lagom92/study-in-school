import requests
from bs4 import BeautifulSoup
import csv

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)
# print(response)

movie_dict = []
soup = BeautifulSoup(response.text, "html.parser")
data_lst = soup.select("ul.lst_detail_t1 > li > dl > dt > a")
for data in data_lst:
    title = data.text
    code = data.attrs['href'].split('code=')[1]
    movie = {
        'title': title,
        'code': code
    }
    movie_dict.append(movie)

# print(movie_dict)


# dict -> csv Save
with open('./naver_movie.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'code'])
    writer.writeheader()
    for data in movie_dict:
        writer.writerow(data)