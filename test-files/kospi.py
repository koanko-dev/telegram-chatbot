# url 요청 => doc 응답 => data 추출
import requests
from bs4 import BeautifulSoup

def get_kospi():
    URL = 'https://finance.naver.com/sise/'

    res = requests.get(URL)

    soup = BeautifulSoup(res.text, 'html.parser')

    kospi = soup.select_one('#KOSPI_now').text
    kosdaq = soup.select_one('#KOSDAQ_now').text
    kospi200 = soup.select_one('#KPI200_now').text

    return f'KOSPI: {kospi}, KOSDAQ: {kosdaq}, KOSPI200: {kospi200}'