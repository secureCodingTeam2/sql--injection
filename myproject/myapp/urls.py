
from django.urls import path
from . import views

# myapp/views.py 파일에 있는 vulnerable_search라는 뷰 함수가 실행
urlpatterns = [
    path('', views.vulnerable_search, name='vulnerable_search'),
]
