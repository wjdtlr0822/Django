
from django.urls import path
from . import views
from app1.models import *

app_name='app1' # {% url 'app1:name' %} 사용할때 필요

urlpatterns = [
    path('list/',views.listStudent,name='list'),
    path('view/<int:num>/',views.ViewStudent),
    path('write/',views.WriteStudent,name='write'),
    path('save/',views.save,name='save'),
    path('rewrite/<int:num>/',views.rewrite,name='rewrite'),
]
