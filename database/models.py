from django.db import models

# Create your models here. 
class Comments_360(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default=" ")  # app名字
    msgid = models.CharField(max_length=255,default="nan")  

class Comments_huawei(models.Model): # 类名代表数据库表名
    # msgid = models.CharField(max_length=255,default="-") 
    nickname = models.CharField(max_length=255,default="anoy") 
    comment = models.CharField(max_length=255,default=" ")
    operTime = models.CharField(max_length=255,default="000000")
    phone = models.CharField(max_length=255,default=" ")
    rating = models.CharField(max_length=255,default="0")
    appname = models.CharField(max_length=255,default="0")

class Comments_xiaomi(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default=" ")  # app名字

class Comments_vivo(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default=" ")  # app名字

class Comments_oppo(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default=" ")  # app名字

class Comments_yingyongbao(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default=" ")  # app名字