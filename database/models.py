from django.db import models

# Create your models here. 
class CommentsList(models.Model): # 类名代表数据库表名
    date = models.CharField(max_length=255,default="000000") 
    user = models.CharField(max_length=255,default="anoy")
    content = models.CharField(max_length=255,default="nan")
    score = models.CharField(max_length=255,default="0")
    version = models.CharField(max_length=255,default=" ")
    name = models.CharField(max_length=255,default="outlook")  # app名字
    msgid = models.CharField(max_length=255,default="nan")  # 主键

    