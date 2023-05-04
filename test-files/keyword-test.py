keyword = input('입력 메시지: ')

if keyword == '주식':
    print('KOSPI: 2490')
    print('KOSDAQ: 842')
    print('KOSPI200: 324')

elif keyword in ['로또', 'lotto', 'Lotto']:
    print('1, 2, 3, 4, 5, 6 100만원')

elif keyword.split()[0] == '쇼핑':
    print('최저가 검색:')
    print(keyword.split()[1])

else:
    print('모르는 명령어 입니다 😢')