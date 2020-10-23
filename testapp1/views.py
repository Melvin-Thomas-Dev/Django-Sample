from django.shortcuts import render
from  django.http import HttpResponse

from .models import todo
# Create your views here.


def index(request):
    t = todo.objects.all() # SELECT * from todo
    return HttpResponse(t[0].text)
