from django.shortcuts import render
from django.http import HttpResponse
from api.models import User
from django.core import serializers

# Create your views here.

def index(request):
    data = serializers.serialize('json', User.objects.only("name","age"))
    return HttpResponse(data, content_type="application/json")
