
"""def write(request):
    if request.method=='POST':                #요청메소드가 post일 경우
        form=Form(request.POST)               # ModelForm에 request.POST를 전송
        if form.is_valid():                   #
            form.save()                       # 웹프레임 워크를 쓰지 않을경우 변수,sql문을 작성하여 넘거야함
            dbCon=dbtest.objects.all()
            return render(request,'list.html',{'dbCon':dbCon})
    else:
        form=Form()                           #request.method가 post가 아닐경우 그냥 출력

    return render(request,'write.html',{'form1':form}) #{'form':form}은 쉽게 form을 만들기 위해
"""

from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from app1.models import *


# Create your views here.
def listStudent(request):
    db=dbtest.objects.all()
    return render(request,'list.html',{'db':db})

def ViewStudent(request,num):
    db=dbtest.objects.get(id=num)
    return render(request,'view.html',{'db':db})

def WriteStudent(request):
    form=Form()
    return render(request,'write.html',{'form':form})

def save(request):
    name=request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    qs=dbtest(name=name,major=major,age=age,grade=grade,gender=gender)
    qs.save()

    return HttpResponseRedirect(reverse('app1:list'))


def rewrite(request,num):
    db=dbtest.objects.get(id=num)
    form=Form(instance=db)
    return render(request,'rewrite.html',{'form':form})