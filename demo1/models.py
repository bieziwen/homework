import datetime

from django.db import models

# Create your models here.

class Goods(models.Model):
    img=models.CharField(max_length=100)
    goods_name=models.CharField(max_length=64)
    details=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    state=models.BooleanField(default=False)
    operation=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)
    class Meta:
        db_table='goods_info'



class Emp(models.Model):
    empname=models.CharField(max_length=32)
    phone=models.CharField(max_length=11)
    email=models.CharField(max_length=32)
    job=models.CharField(max_length=32)
    join_time=models.DateTimeField(datetime.datetime.now())
    state=models.BooleanField(default=False)
    operation=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)

    class Meta:
        db_table='emp'

