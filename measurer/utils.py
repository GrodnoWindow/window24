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
                       status, final_amount, executor, file=None, ):
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

    if not (executor == '0'):
        user = User.objects.get(pk=int(executor))
        measurement.executor = user

    if file == None:
        pass
    else:
        measurement.agreements = file

    measurement.save()


def update_log(request, pk, client, address, number, time, comment, date,
               status, final_amount, executor, file=None):
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    measurement = Measurement.objects.get(pk=pk)
    if not (measurement.client == client):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил имя клиента с "{measurement.client}" на "{client}";'
    if not (measurement.address == address):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил адрес с "{measurement.address}" на "{address}";'
    if not (measurement.number == number):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил номер телефона с "{measurement.number}" на "{number}";'
    if not (measurement.time == time):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил время замера с "{measurement.time}" на "{time}";'
    if not (measurement.comment == comment):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил комментарий с "{measurement.comment}" на "{comment}";'
    if not (measurement.date == date):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил дату замера с "{measurement.date}" на "{date}";'
    if not (measurement.status == status):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил статус с "{measurement.status}" на "{status}";'
    if not (measurement.final_amount == final_amount):
        measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил окончательную сумму просчета с "{measurement.final_amount}" на "{final_amount}";'
    if not (measurement.executor == executor):
        if not (executor == "0"):
            user = User.objects.get(pk=int(executor))
            measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил исполнителя с "{measurement.executor}" на "{user.first_name} {user.last_name}";'
    if not (measurement.agreements == file):
        if not (file == None):
            measurement.logs = measurement.logs + f'Пользователь: "{request.user.username}" {dt} изменил файл с "{measurement.agreements}" на "{file}";'

    measurement.save()
