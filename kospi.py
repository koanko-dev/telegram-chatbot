# url 요청 => doc 응답 => data 추출
import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'

res = requests.get(URL)

soup = BeautifulSoup(res.text, 'html.parser')

kospi = soup.select_one('#KOSPI_now').text

print(kospi)