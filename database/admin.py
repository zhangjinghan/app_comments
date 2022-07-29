from django.contrib import admin

# Register your models here.

from .models import CommentsList

admin.site.register(CommentsList)