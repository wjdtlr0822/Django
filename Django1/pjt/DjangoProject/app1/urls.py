
from django.urls import path
from . import views  #현재폴더의 views.py를 import

urlpatterns = [
    path('index/',views.index,name='index'),
    path('aw/',views.write,name='write'), #'aw' 는 주소 view.write는 view안에 write라는 함수
    path('list/',views.list,name='list'),
]
