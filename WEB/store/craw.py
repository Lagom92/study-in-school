from bs4 import BeautifulSoup
import requests
import json

import requests

headers = {
    'authority': 'search.shopping.naver.com',
    'accept': 'application/json, text/plain, */*',
    'urlprefix': '/api',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?origQuery=%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=2DXFQWWYWMBF6; NID_AUT=1KEFX7r7cDK5NJ+lQQai1ViWc0Y3wEwBDQhV+XkpfjERH4xkhpi6w3oQ8i0JrxS1; NID_JKL=YDgy1bSpoViHlqfBSqIPbnU9dgOw7HfF+ywLS0TxmdQ=; NRTK=ag#20s_gr#2_ma#-2_si#0_en#0_sp#-2; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga=GA1.1.1354024770.1594886521; _ga_4BKHBFKFK0=GS1.1.1594888370.1.1.1594888979.53; ASID=dc5f2a11000001738631025900000065; AD_SHP_BID=4; nx_ssl=2; page_uid=UzupCwp0Yihss7rMIj4ssssstXl-252384; NID_SES=AAABiVJJc90cRSMy6XUkCUO+68IiNY2DgI23pVFadJtHtADNqcV5uMYytdyMtQY6wsho3aWK9cJv6TzNesytGGoYF0W1QqDdjlO530Id+w7qtie77Br3aXad/3ql/FtzEwFlJJU+bxFC1O4p4gJAH4SynvBf5484octAD5QlFNRa0X81NK+wk4x3whuXsU4yd1xXXaePHY/cQzW/kda8AfD+aopybjGzS2U514y/TOa8tDfWdyIoIKa9LW85ED/qc2dlFpFICiZxEbRW0Kn2pUI+8Uy338HMx/bSAPav0bqLt14A6JBcrG78frFUXMgyL9C04Q6bgXiOymO6qQg7608nt8Rpsoj5EBdBAf15ksxwbeZ1y2By7Aj7noY3rIeQ6WM3lwqPanoCsNLG7dVLDXKIo0pW2BLkcIa5mSmMhDWq7r2+DIEscw7O5d2osIiRV4FDmOymDZDyF8gpn5f2eJn4WgdwbU6hYOrJxlJAVVzt/fj8EwwvBWlCmnn8SMoBch21UVYOKEGA9zrLDWHgLCuV9+w=; spage_uid=UzupCwp0Yihss7rMIj4ssssstXl-252384; JSESSIONID=BAD148F2D39E5B00062436565A97652C',
}

params = (
    ('sort', 'rel'),
    ('pagingIndex', '2'),
    ('pagingSize', '40'),
    ('viewType', 'list'),
    ('productSet', 'total'),
    ('query', '\uB9C8\uC6B0\uC2A4'),
    ('origQuery', '\uB9C8\uC6B0\uC2A4'),
    ('iq', ''),
    ('eq', ''),
    ('xq', ''),
)

response = requests.get('https://search.shopping.naver.com/search/all', headers=headers, params=params)

data = response.json()

lst = data['searchAdResult']['products']
for i in lst:
    print(i['productTitle'])
    print(i['price'], '원')


