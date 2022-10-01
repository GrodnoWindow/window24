from call.models import Call
from client.models import Client, Number


def create_number_record(number):
    Number.objects.create(number=number)
    return Number.objects.all().values('id').order_by('-id')[:1]


def search_calls_client():
    pass


# def add_calls_to_client(Client):
#     id_client = Client.objects.filter(id='id')
