from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^info/$', views.info, name='info'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
   url(r'^goods/$', views.goods, name='goods'),
    url(r'addcart/$', views.addcart, name='addcart'),
    url(r'subcart/$', views.subcart, name='subcart'),

    url(r'changecart/$', views.changecart, name='changecart'),
    url(r'^changeselect/$', views.changeselect, name='changeselect'),
    url(r'generateorder/$', views.generateorder, name='generateorder'),
    url(r'^orderinfo/$', views.orderinfo, name='orderinfo'),
    url(r'^changeorder/$', views.changeorder, name='changeorder'),

url(r'^logout/$', views.logout, name='logout')]
