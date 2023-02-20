import datetime

import requests, csv
import time

from call.models import CallWindow, CallOkna, CallOkna, CallWindow

from client.models import Client, Number

from client.utils import create_calls_record

from calls_table.models import CallsTable

# from client.models import Client



def parse_csv_file():
    with open('call-history.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row[0])


def save_all_calls():
    parse_csv_file()