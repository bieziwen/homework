from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from demo1.models import Goods, Emp


def index(request):
    good=Goods(img='http://www.27270.com/word/fengjingsheying/2018/307087.html'
               ,goods_name='大头娃娃',details='大头娃娃头很大',price='555.00')
    good.save()
    return HttpResponse('添加信息')

def test1(request):
    goods=Goods.objects.all()
    return render(request,'test1.html',{'goods':goods})


def test2(request):
    emps=Emp.objects.all()
    return render(request,'test2.html',{'emps':emps})