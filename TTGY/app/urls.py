from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),

    url(r'^info/(\d+)$', views.info, name='info'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
url(r'^cart/$', views.cart, name='cart')
]
