from dotenv import load_dotenv
import os
import requests

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'

# 1. 수신한 메시지를 확인한다.
response = requests.get(BASE_URL + '/getUpdates').json()

last_chat_id = response['result'][-1]['message']['chat']['id']
last_msg = response['result'][-1]['message']['text']

# 2. 메시지에 따라 정해진 답을 준비한다.
reply_msg = last_msg + '!!'

# 3. 준비된 답을 회신한다.
requests.get(BASE_URL + f'/sendMessage?chat_id={last_chat_id}&text={reply_msg}')