from django.http import HttpResponse
from database.models import CommentsList
from django.core import serializers


def comments(request):
    data = CommentsList.objects.all()
    res = serializers.serialize('json', queryset=data)
    return HttpResponse(res)
