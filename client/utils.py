from call.models import Call
from client.models import Client, Number, Address


def create_number_record(number):
    check_number = Number.objects.filter(number=number)
    if not check_number:
        Number.objects.create(number=number)
    else:
        return False
    return Number.objects.all().values('id').order_by('-id')[:1]


def create_calls_record(number):
    calls = Call.objects.filter(number=number).values('id').order_by('-id')
    return calls

def create_address_record(address):
    Address.objects.create(name=address)
    return Address.objects.all().values('id').order_by('-id')[:1]




# def add_calls_to_client(Client):
#     id_client = Client.objects.filter(id='id')
