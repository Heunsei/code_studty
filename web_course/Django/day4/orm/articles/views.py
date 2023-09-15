from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    # DB에서 전체 게시글을 조회 해야함
    articles = Article.objects.all()
    # 받은 전체 게시글 데이터를 저장해서 변수에 저장
    # index 템플릿에서 사용할 수 있도록 전달
    context = {
        'articles' : articles,
    }
    return render(request, 'index.html', context)