from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def write(request):
    if request.method=='POST':                #요청메소드가 post일 경우
        form=Form(request.POST)               # ModelForm에 request.POST를 전송
        if form.is_valid():                   #
            form.save()                       # 웹프레임 워크를 쓰지 않을경우 변수,sql문을 작성하여 넘거야함
            dbCon=dbtest.objects.all()
            return render(request,'list.html',{'dbCon':dbCon})
    else:
        form=Form()                           #request.method가 post가 아닐경우 그냥 출력

    return render(request,'write.html',{'form1':form}) #{'form':form}은 쉽게 form을 만들기 위해


def list(request):
    dbCon=dbtest.objects.all()                    #dbtest에 있는 모든  object(내용)을 가져옴
    return render(request,'list.html',{'dbCon':dbCon})

def view(request,num):
    dbCon=dbtest.objects.get(id=num)                 # model에 대한 id가 무조건 생성된다(?)
    return render(request,'view.html',{'dbCon':dbCon})