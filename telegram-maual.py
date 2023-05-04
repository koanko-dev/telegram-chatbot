import requests
from dotenv import load_dotenv
import os

import utils

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

response = requests.get(BASE_URL + '/getUpdates').json()

last_chat_id = response['result'][-1]['message']['chat']['id']
last_msg = response['result'][-1]['message']['text']

if last_msg == '주식':
    return_msg = utils.get_kospi()

elif last_msg in ['로또', 'lotto', 'Lotto']:
    return_msg = utils.get_lotto()

elif last_msg.split()[0] == '쇼핑':
    item = last_msg.split()[1]
    return_msg = utils.get_naver_shopping(item)

else:
    return_msg = '모르는 명령어 입니다 😢'


requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={return_msg}')