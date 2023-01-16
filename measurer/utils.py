from datetime import datetime

from .models import Measurement
from .models import *

def get_measurements(date):
    return Measurement.objects.filter(date=date)


def update_measurement(request,pk, client, address, number, time, comment, date, status):
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
    measurement.save()