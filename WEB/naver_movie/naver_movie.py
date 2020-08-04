import requests
from bs4 import BeautifulSoup
import csv


def get_movie_data():
    URL = "https://movie.naver.com/movie/running/current.nhn"
    response = requests.get(URL)
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
    return movie_dict


def save_to_csv(movie_dict):
    # dict -> csv
    with open('./naver_movie.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'code'])
        writer.writeheader()
        for data in movie_dict:
            writer.writerow(data)

# def get_comment(code):
#     detail_URL = f"https://movie.naver.com/movie/bi/mi/basic.nhn?code={code}"
#     response = requests.get(detail_URL)
#     print(response)

#     soup = BeautifulSoup(response.text, "html.parser")
#     ul = soup.select("div.score > div.score_result > ul")

#     for p in ul:
#         comments = p.select("div.score_reple > p")
#         scores = p.select("div.star_score > em")

#         for c, s in zip(comments, scores):
#             comment = c.text.strip()
#             score = s.text

#             print(comment, score)

def main():
    movie_dict = get_movie_data()
    save_to_csv(movie_dict)

    # movie_dict = movie_dict[:3]

    # for data in movie_dict:
    #     code = data['code']

    #     get_comment(code)
            
        

        
            


        



main()