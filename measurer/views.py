from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .utils import *


# Create your views here.


def index(request):
    if request.method == "GET":
        date = request.GET.get('calendar')
        if date is None or date == "":
            date = datetime.now().date()
        get_measurements(date)

    if request.method == "POST":
        date = request.GET.get('calendar')
        if date is None or date == "":
            date = datetime.now().date()
        pk = request.POST.get('pk')
        client = request.POST.get('client')
        address = request.POST.get('address')
        number = request.POST.get('number')
        time = request.POST.get('time')
        date_measurement = request.POST.get('calendarMeasurement')
        comment = request.POST.get('comment')
        status = request.POST.get('select')
        update_measurement(pk=pk, client=client,
                           address=address,
                           number=number,
                           time=time,
                           date=date_measurement,
                           comment=comment,
                           status=status)

    context = {
        'measurements': get_measurements(date),
    }
    return render(request, "measurer/index.html", context)
