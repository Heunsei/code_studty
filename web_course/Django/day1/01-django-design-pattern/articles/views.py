from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인 페이지 응답
    return render(request, 'articles/index.html')
