from django.db import models
import requests
# Create your models here.
# Book이란 class를 정의 한곳
# db에 영향을 끼치는 부분은 models. 로 가져온 field를 정의한것
# model class 상속받아서 부분들

# 나머지는 모두 python
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField()
    pub_date = models.DateField()
    
    @classmethod
    def insert_data(cls):
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
        response = requests.get(URL, params=params)
        data = response.json()
        for item in data['item']:
            params = {
                'isbn' : item['isbn'],
                'title' : item['title'],
                'pub_date' : item['pubDate']
            }
            # dict 를 언패킹해서 넣어줌
            # 밑의 주석과 똑같은 말임
            book = cls(**params)
            book.save()

    '''
    variable = modelClass(key=value,key=value)
    book = Book(~~데이터저장~~)
    '''