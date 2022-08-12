import imp
import django
from django.http import HttpResponse
from django.shortcuts import render
from database import models
from django.core import serializers
 
def get_360(request):
    results = models.Comments_360.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)

def get_huawei(request):
    results = models.Comments_huawei.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)

def get_xiaomi(request):
    results = models.Comments_xiaomi.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)

def get_vivo(request):
    results = models.Comments_vivo.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)

def get_oppo(request):
    results = models.Comments_oppo.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)

def get_yingyongybao(request):
    results = models.Comments_yingyongbao.objects.all()
    components = serializers.serialize("json", queryset=results)
    return HttpResponse(components)
