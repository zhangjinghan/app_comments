from django.contrib import admin

# Register your models here.

from .models import Comments_360,Comments_huawei

admin.site.register(Comments_360)
admin.site.register(Comments_huawei)