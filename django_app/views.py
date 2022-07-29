import imp
import django
from django.http import HttpResponse
from django.shortcuts import render
from database import models
from django.core import serializers
 
def getcomments(request):
    results = models.CommentsList.objects.all()
    components = serializers.serialize("json", queryset=results)

    return HttpResponse(components)