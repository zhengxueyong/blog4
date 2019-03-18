import hashlib
import random

import os
import random
import time
import uuid

import time

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.cache import cache
# Create your views here.
from app.models import Goods, User


def index(request):
    token=request.session.get('token')
    user=None
    if token:
        user=User.objects.get(token=token)
    goods=Goods.objects.all()


    return render(request,'index.html' ,context={'user':user })

def cart(request):
    return render(request,'cart.html')

def info(request):
    return render(request,'info.html')



def goods(request, num=1):
    goods_List = Goods.objects.all()

    # 缓存
    # value = cache.get(key)
    token = cache.get('token', '不存在')
    print(token)


    return render(request, 'goods.html', context={'goods_List':goods_List})



def genrate_token():
    token = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


def genrate_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


def register(request):
    if request.method=='GET':

        return render(request,'register.html')
    elif request.method=='POST':

        phone_num=request.POST.get('phone_num')
        password=request.POST.get('password')
        try:
            user=User()

            user.t_phone=phone_num
            user.t_password=genrate_password(password)
            user.token=genrate_token()
            user.save()
            response=redirect("app:index")
            request.session['token']=user.token
            return response
        except:
            return render(request,'index.html')


def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        phone_num = request.POST.get('phone_num')

        password=request.POST.get('password')
        users=User.objects.filter(t_phone=phone_num).filter(t_password=genrate_password(password))
        if users.exists():
            user=users.first()
            user.token=genrate_token()
            user.save()
            response=redirect('app:index')
            request.session['token']=user.token
            return response
        else:
            return render(request,'index.html')


def goods(request,index=1):

    token=request.session.get('token')
    users=User.objects.filter(token=token)
    good=Goods.objects.get(id=index)
    if users.exists():

        return render(request,'goods.html',context={'good':good})
    else:

        return render(request,'login.html')


def logout(request):
    request.session.flush()
    response=redirect('app:index')


    return response




def addcart(request):
    goodsid = request.GET.get('goodid')
    print(goodsid)
    token=request.session.get('token')
    user=User.objects.get(token=token)
    good=Goods.objects.get(pk=goodsid)


    response_data = {
        'staus': 1
    }


    return JsonResponse(response_data)




