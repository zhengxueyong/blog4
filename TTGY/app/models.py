from django.db import models

# Create your models here.
class Goods(models.Model):
    # 商品名称
    name = models.CharField(max_length=20)
    # 商品图片
    icon = models.CharField(max_length=255)
    # 商品价格
    price = models.IntegerField()
    # 商品描述
    detail = models.CharField(max_length=255)

    class Meta:
        db_table = 'goods'


class User(models.Model):
    # 电话号码
    t_phone = models.CharField(max_length=40)
    # 密码
    t_password = models.CharField(max_length=256)
    token = models.CharField(max_length=256)



