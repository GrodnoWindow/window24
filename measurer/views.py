from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
from .forms import *


# Create your views here.


def index(request):
    if request.method == "GET":
        date = request.GET.get('calendar')
        if date is None or date == "":
            date = datetime.now().date()
        # get_measurements(request,date)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
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
        final_amount = request.POST.get('final_amount')
        executor = request.POST.get('selectMeasurers')
        try:
            file = request.FILES['image']
        except:
            file = None

        update_log(request=request,
                   pk=pk, client=client,
                   address=address,
                   number=number,
                   time=time,
                   date=date_measurement,
                   comment=comment,
                   status=status,
                   final_amount=final_amount,
                   file=file,
                   executor=executor, )

        update_measurement(request=request,
                           pk=pk, client=client,
                           address=address,
                           number=number,
                           time=time,
                           date=date_measurement,
                           comment=comment,
                           status=status,
                           final_amount=final_amount,
                           file=file,
                           executor=executor,
                           )

        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    # agreements = Agreements.objects.all()

    context = {
        'measurements': get_measurements(request,date),
        'form': form,
        # 'agreements': agreements,
        'measurers': get_measurers(),
    }
    return render(request, 'measurer/index.html', context)

