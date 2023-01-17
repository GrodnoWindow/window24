from datetime import datetime

from rest_framework.permissions import IsAuthenticated

from .models import Measurement
from .models import *
from django.utils.datastructures import MultiValueDict
from users.models import User
from users.views import AuthenticatedUser


def get_measurers():
    return User.objects.filter(measurer=True)


def get_measurements(request, date):
    user = request.user
    if user.is_superuser:
        return Measurement.objects.filter(date=date)
    elif user.measurer:
        return Measurement.objects.filter(date=date, executor=user)


def update_measurement(request, pk, client, address, number, time, comment, date,
                       status, final_amount, executor, file=None,):
    user = request.user.first_name
    measurement = Measurement.objects.get(pk=pk)
    measurement.client = client
    measurement.address = address
    measurement.number = number
    measurement.time = time
    measurement.comment = comment
    measurement.date = date
    measurement.status = status
    measurement.final_amount = final_amount
    measurement.time_updated = datetime.now()
    measurement.who_updated = user

    if not(executor == '0'):
        user = User.objects.get(pk=int(executor))
        measurement.executor = user

    if file == None:
        pass
    else:
        measurement.agreements = file

    measurement.save()
