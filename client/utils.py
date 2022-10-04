from call.models import Call
from client.models import Client, Number


def create_number_record(number):
    Number.objects.create(number=number)
    return Number.objects.all().values('id').order_by('-id')[:1]


def create_calls_record(number):
    calls = Call.objects.filter(number=number).values('id').order_by('-id')
    # print(f'CALLS : {calls}')
    return calls



# def add_calls_to_client(Client):
#     id_client = Client.objects.filter(id='id')
