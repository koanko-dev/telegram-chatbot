import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_naver_shopping(search_keyword):
    naver_id = os.getenv('NAVER_CLINET_ID')
    naver_secret = os.getenv('NAVER_CLIENT_SECRET')

    URL = 'https://openapi.naver.com/v1/search/shop.json?query='+search_keyword
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret,
    }

    res = requests.get(URL, headers=headers).json()
    result = res['items'][0]
    msg = f"{result['title']} : {result['lprice']} \n {result['link']}"
    
    return msg
