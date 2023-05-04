import requests
from dotenv import load_dotenv
import os

load_dotenv()

naver_id = os.getenv('NAVER_CLINET_ID')
naver_secret = os.getenv('NAVER_CLIENT_SECRET')

URL = 'https://openapi.naver.com/v1/search/shop.json?query=캣그라스'
headers = {
    'User-Agent': 'curl/7.49.1',
    'X-Naver-Client-Id': naver_id,
    'X-Naver-Client-Secret': naver_secret,
}

res = requests.get(URL, headers=headers)

print(res.text)
