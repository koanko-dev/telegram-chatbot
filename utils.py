import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def get_kospi():
    URL = 'https://finance.naver.com/sise/'
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, 'html.parser')
    kospi = soup.select_one('#KOSPI_now').text
    kosdaq = soup.select_one('#KOSDAQ_now').text
    kospi200 = soup.select_one('#KPI200_now').text
    return f'KOSPI: {kospi}, KOSDAQ: {kosdaq}, KOSPI200: {kospi200}'

def get_lotto():
    URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1065'
    res = requests.get(URL)
    data = res.json()
    numbers = []
    for i in range(1, 7):
        numbers.append(data[f'drwtNo{i}'])
    return f"번호: {numbers}, 보너스: {data['bnusNo']}, 상금: {data['firstWinamnt']}"

def get_naver_shopping(item):
    NAVER_CLINET_ID = os.getenv('NAVER_CLINET_ID')
    NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')

    URL = f'https://openapi.naver.com/v1/search/shop.json?query={item}'

    headers = {
        'X-Naver-Client-Id': NAVER_CLINET_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
    }

    res = requests.get(URL, headers=headers).json()
    result = res['items'][0]
    msg = f"{result['title']}) {result['lprice']}원 \n {result['link']}"
    return msg