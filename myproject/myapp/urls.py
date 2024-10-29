
from django.urls import path
from . import views

# myapp/views.py 파일에 있는 vulnerable_search라는 뷰 함수가 실행
urlpatterns = [
    path('', views.vulnerable_search, name='vulnerable_search'),  # 'name='vulnerable_search''라는 url 패턴에 이름을 부여하여 템플릿을 통해 이 url을 참조할 수 있게 함.
]
