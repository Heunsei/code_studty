import requests
# 파이썬으로 api에 요청보내기
# pip install requests
# pip freeze > requirements.txt


API_KEY = 'ttbgms2451703001'
params = {
    'ttbkey': API_KEY,
    'Query' : 'Aladin',
    'QueryType' : 'ItemNewAll',
    'MaxResults' : 10,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101'
}
URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
# url/?key=value&key=value
# request.get(URL, params)
response = requests.get(URL, params=params)
data = response.json()
# data['item'] -> [] 각 책 데이터 들이 dict로 들어있음
#print(data['item'])
for item in data['item']:
    print(item['isbn'])
    print(item['title'])
    print(item['pubDate'])
