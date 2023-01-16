from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
# Create your views here.


def index(request):

    context = {
        'ticketsInWork': 1,
    }
    return render(request, "measurer/index.html", context)
