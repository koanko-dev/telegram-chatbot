import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1065'
res = requests.get(URL)

data = res.json()

numbers = []

for i in range(1, 7):
    numbers.append(data[f'drwtNo{i}'])

return_msg = f"번호: {numbers}, 보너스: {data['bnusNo']}, 상금: {data['firstWinamnt']}"
print(data['bnusNo'])
print(data['firstWinamnt'])