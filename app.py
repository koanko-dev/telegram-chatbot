from flask import Flask, request
import requests
from dotenv import load_dotenv
import os

import utils

load_dotenv()

app = Flask('telegram-chatbot')

TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
URL = BASE_URL + '/setWebhook?url=https://970c-220-86-211-89.ngrok-free.app/telegram'

@app.route('/telegram', methods=['POST'])
def telegram():
    data = request.json
    print('요청')
    chat_id = data['message']['from']['id']
    message = data['message']['text']

    if message == '주식':
        return_msg = utils.get_kospi()

    elif message in ['로또', 'lotto', 'Lotto']:
        return_msg = utils.get_lotto()

    elif message.split()[0] == '쇼핑':
        item = message.split()[1]
        return_msg = utils.get_naver_shopping(item)

    else:
        return_msg = '모르는 명령어 입니다 😢'


    requests.get(BASE_URL + f'/sendMessage?chat_id={chat_id}&text={return_msg}')

    return 'Telegram CHATBOT'

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(port=5000, debug=True)