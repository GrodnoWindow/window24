from datetime import datetime

from .models import Measurement
from .models import *
from django.utils.datastructures import MultiValueDict
def get_measurements(date):
    return Measurement.objects.filter(date=date)


def update_measurement(request,pk, client, address, number, time, comment, date, status,file = None):
    user = request.user.first_name
    measurement = Measurement.objects.get(pk=pk)
    measurement.client = client
    measurement.address = address
    measurement.number = number
    measurement.time = time
    measurement.comment = comment
    measurement.date = date
    measurement.status = status
    measurement.time_updated = datetime.now()
    measurement.who_updated = user
    if file == None:
        pass
    else:
        measurement.agreements = file


    measurement.save()

