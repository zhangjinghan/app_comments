from django.db import models


# Create your models here.
class CommentsList(models.Model):
    date = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    name = models.CharField(max_length=255)  # app名字
    id = models.AutoField(primary_key=True)  # 主键
