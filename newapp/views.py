from django.shortcuts import render
from django.http import HttpResponse

from .forms import IndexForm

# Create your views here.

def index(request):
    return HttpResponse('made it')