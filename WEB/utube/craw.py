import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.youtube.com',
    'x-youtube-sts': '18484',
    'x-youtube-device': 'cbr=Chrome&cbrver=84.0.4147.105&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0',
    'x-youtube-page-label': 'youtube.ytfe.desktop_20200805_1_RC1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'x-youtube-variants-checksum': '6a861b7b1aba897f0ac7f471b14e2372',
    'x-youtube-page-cl': '325146078',
    'x-spf-referer': 'https://www.youtube.com/results?search_query=%EC%95%84%EC%9D%B4%EC%9C%A0',
    'x-youtube-utc-offset': '540',
    'x-youtube-client-name': '1',
    'x-spf-previous': 'https://www.youtube.com/results?search_query=%EC%95%84%EC%9D%B4%EC%9C%A0',
    'x-youtube-client-version': '2.20200806.01.01',
    'dpr': '1.25',
    'x-youtube-time-zone': 'Asia/Seoul',
    'x-youtube-ad-signals': 'dt=1597147010507&flash=0&frm&u_tz=540&u_his=3&u_java&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&u_nplug=3&u_nmime=4&bc=31&bih=722&biw=818&brdim=0%2C0%2C0%2C0%2C1536%2C0%2C1536%2C824%2C834%2C722&vis=1&wgl=true&ca_type=image',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.youtube.com/results?search_query=%EC%95%84%EC%9D%B4%EC%9C%A0',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'VISITOR_INFO1_LIVE=HVHzPL8QXDw; YSC=h-QagUPD9TM; GPS=1; PREF=f4=4000000; ST-1bm6gjx=oq=%EC%95%84%EC%9D%B4%EC%9C%A0&gs_l=youtube.12...0.0.1.41128.0.0.0.0.0.0.0.0..0.0.ytfpa2%2Cytpo-lf%3D0%2Cytposo-lf%3D0%2Ccfro%3D1...0...1ac..64.youtube..0.0.0....0.BfP3J0ICxso&itct=CBkQ7VAiEwimpvakjJPrAhVMVSoKHX-8A-w%3D&csn=iYcyX8f0C8u5gQOig6jIBA',
}

params = (
    ('search_query', '\uC544\uC774\uC720'),
    ('pbj', '2'),
)

response = requests.get('https://www.youtube.com/results', headers=headers, params=params)
# print(response)
data = response.json()
contents = data[1]['response']['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']

video_url = "https://www.youtube.com/watch?v="

for idx, content in enumerate(contents):
    video_link = ''
    video_title = ''
    try:
        video_link = video_url + contents[idx]['videoRenderer']['videoId']
        video_title = contents[idx]['videoRenderer']['title']['runs'][0]['text']

        print(video_link)
        print(video_title)
    except:
        pass

    if idx == 5:
        break

    
# 후반 과정
# 영상의 id 값을 이용해서 광고 없는 영상 가져오기
