from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import csv
import os


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
    with open(f'./movie.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'code'])
        writer.writeheader()
        for data in movie_dict:
            writer.writerow(data)


def get_score(title, code, headers):
    params = (
        ('code', code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    soup = BeautifulSoup(response.text, "html.parser")
    ul = soup.select("body > div > div > div.score_result > ul > li")

    data_list = []
    for i, res in enumerate(ul):
        score = res.select_one("div.star_score > em").text
        comment = ''
        if res.select_one(f'div.score_reple > p > span#_filtered_ment_{i} > span#_unfold_ment{i}') is None:
            comment = res.select_one(
                f'div.score_reple > p > span#_filtered_ment_{i}').text.strip()
        elif res.select_one(f'div.score_reple > p > span#_filtered_ment_{i} > span#_unfold_ment{i}'):
            comment = res.select_one(
                f'div.score_reple > p > span#_filtered_ment_{i} > span > a')['data-src']

        data = {
            'title': title,
            'code': code,
            'comment': comment,
            'score': score,
        }
        data_list.append(data)

    return data_list


def main():
    movie_dict = get_movie_data()
    save_to_csv(movie_dict)

    headers = {
        'authority': 'movie.naver.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=2DXFQWWYWMBF6; NID_AUT=1KEFX7r7cDK5NJ+lQQai1ViWc0Y3wEwBDQhV+XkpfjERH4xkhpi6w3oQ8i0JrxS1; NID_JKL=YDgy1bSpoViHlqfBSqIPbnU9dgOw7HfF+ywLS0TxmdQ=; NRTK=ag#20s_gr#2_ma#-2_si#0_en#0_sp#-2; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.1.1354024770.1594886521; _ga_4BKHBFKFK0=GS1.1.1594888370.1.1.1594888979.53; ASID=dc5f2a11000001738631025900000065; nx_ssl=2; BMR=s=1596679002468&r=https%3A%2F%2Fm.blog.naver.com%2Fso576%2F221753254561&r2=https%3A%2F%2Fwww.google.com%2F; page_uid=UyWB9lprvxsssaonm2VssssstnG-499437; NID_SES=AAABiPx/czMCesVgjXfEf3+2k0vfSOovPsi6N5fdu/nptlqq1fjtXBehRcRfL8KFMR6xx68a/3XInioCAJILeew6Ym7a+yLV5kvTmI8iq4xI0q+8ks8fUhZ/8KwVamc/XY0/Wlg4yROtAA2A5X/vExGEj+GW/oCw/pLbXOR/kVVdcPODR17ORqQcVIcWfE+a2r5NrfjyuRtEnNAW7Kp+Uf9JIVYR5FC7D/l+2T1j3TA3ozPS36R1LMQ5yaGg2bpIA46nA6PS/YCMzLI1ZVD5x70k5JJjOlqaGG+EwhsEVHkjDdi1EAJwXE2g860kHWlRyfZsWu9ble6ul7FgGY5pfPOevH9hziPuKCe+LsAhfDMKattKBz/C9k/4Ile3M5llxCezySYm3/ufkQlcj95aXrOLdpXlNREOBtW/ryL2Q3g6ShfVuba+THZrw6kNjDlVbDPSTpuyYqVZbmp7LRr2u0asYTNNAstUQgCXShFxbqVP+uSEGULdp40RDwlhwA5SYQYRgdvRbNsSz82uuX2OHXTvzC0=; csrf_token=b5e624f3-2dec-4f35-b693-3e23ddc366ff',
    }

    # score_dict = get_score("188909", headers)
    # movie_dict = movie_dict[:3]

    os.makedirs('./movie', exist_ok=True)
    with open(f'./movie/score.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'code', 'comment', 'score'])
        writer.writeheader()

        for movie in tqdm(movie_dict):
            code = movie['code']
            title = movie['title']
            score_dict = get_score(title, code, headers)
            
            # save
            for data in score_dict:
                writer.writerow(data)
        

if __name__ == "__main__":
    main()
