from django.shortcuts import render

# Create your views here.
def index(request):
    # 메인 페이지 응답
    # 되도록 convention 지켜서 request사용
    # request 사용자의 요청에 대한 모든 정보
    # 두번째 인자는 정확히 템플릿이 위치한 경로
    return render(request, 'index.html')
