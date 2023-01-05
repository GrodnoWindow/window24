from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Index(request):
    # parserJson()
    # ticketsInWork = inWork()
    # ticketsInQueue = allInQueue()  # вся очередь
    context = {
        'ticketsInWork': 1,
    }
    return render(request, "measurer/index.html", context)
