from django.shortcuts import render
import random

# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육']
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked' : picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(request.META)
    # 사용자로부터 요청을 받아서
    # 요청에서 사용자 입력을 찾아야함
    # context에 저장하고 catch 템플릿에 출력
    print(request.GET.get('message'))
    message = request.GET.get('message')
    context = {
        'message' : message,
    }

    return render(request, 'articles/catch.html' , context)

def greeting(request, name):
    # request 에 사용자가 보낸 정보가 들어있음
    context = {
        'name' : name,
    }
    return render(request, 'articles/greeting.html', context)

def details(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)
