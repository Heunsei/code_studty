from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.show, name='show'),
    path('<author_name>/', views.detail, name='detail'),
]
