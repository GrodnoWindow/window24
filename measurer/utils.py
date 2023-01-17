from datetime import datetime

from rest_framework.permissions import IsAuthenticated

from .models import Measurement
from .models import *
from django.utils.datastructures import MultiValueDict
from users.models import User
from users.views import AuthenticatedUser

def login_in():
    user = User.objects.get(username='test1')
    if user.password == 'тестовый пароль':
        print('НУ ВСЕ ИЗИ ЕБАТЬss')
    else:
        print('вилы пизда')


def get_measurements(date):
    return Measurement.objects.filter(date=date)


def update_measurement(request, pk, client, address, number, time, comment, date, status, final_amount, file=None):
    login_in()
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
    if file == None:
        pass
    else:
        measurement.agreements = file

    measurement.save()
