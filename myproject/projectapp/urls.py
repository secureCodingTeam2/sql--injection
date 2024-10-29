from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index, name='index'),  # 기본 경로에 대해 'index' 뷰 실행
   path('', views.safe_search, name='safe_search'),
]
