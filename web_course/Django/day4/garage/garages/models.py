from django.db import models

# Create your models here.
class Garage(models.Model):
    location = models.CharField(max_length=200) 
    capacity = models.IntegerField()
    is_parking_avaliable = models.BooleanField()
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)

# makemigrations    > 설계도 작성
# migrate           > table 생성

# 조회
# ORM > python object 다루는 방법
# myModel_Class_name.manager.QuerySet Api
# garages = Garage.objects.all()
# print(garages)

# 생성

# python object
# garage = Garage()
# garage.location = '잉잉잉'
# garage.capacity = 10
# garage.is_parking_avaliable = True
# garage.opening_time = '07:00'
# garage.closing_time = '23:00'
# print(garage.locaton)

# QuerySey API
# garage1 = Garage.objects.create(location = '울산광역시', capacity = 22, is_parking_avaliable=True,opening_time='07:00',
#                      closing_time='23:00')

# 삭제
# 삭제가 완료되면 완료된 객체정보를 반환
# garage2.delete()

# garages = <querySet []>
# 파이썬 리스트랑 똑같이 쓸수 있다

# g = Garage.objects.get(pk=2)
# g를 id 2번에 대한 접근변수로 사용가능