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
from app.models import Goods, User, OrderGoods, Cart, Order

def index(request):
    token=request.session.get('token')
    user=None
    if token:
        user=User.objects.get(token=token)
    goods=Goods.objects.all()



    return render(request,'index.html' ,context={'user':user ,'goods':goods})
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


def info(request,index=1):
    token = request.session.get('token')
    users = User.objects.filter(token=token)
    good = Goods.objects.get(id=index)
    if users.exists():

        return render(request, 'info.html', context={'good': good})
    else:

        return render(request, 'login.html')
def cart(request,index=1):
    carts=Cart.objects.get(id=index)
    return render(request, 'cart.html', context={'carts': carts})

def genrate_token():
    token = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))

    return md5.hexdigest()


def genrate_password(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()









def logout(request):
    request.session.flush()
    response=redirect('app:index')
    return response


