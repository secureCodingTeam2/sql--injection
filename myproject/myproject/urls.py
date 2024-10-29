from django.contrib import admin                  #Django의 기본 관리자(admin) 인터페이스를 활성화하기 위한 모듈
from django.urls import include, path             #

urlpatterns = [
    path('admin/', admin.site.urls),              # 관리자 페이지를 /admin/ URL에 연결
    path('myapp/', include("myapp.urls")),
    path('projectapp/', include("projectapp.urls")),
]
