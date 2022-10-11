import datetime

import requests, csv
import time

from call.models import Call, Call_Okna

from client.models import Client, Number

# from client.models import Client



def get_credentials():
    login_session = requests.Session()

    login_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
    }

    login_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Session.login",
        "params": {
            "userName": LOGIN,
            "password": PASSWORD,
            "application": {
                "name": "Test",
                "vendor": "Keiro",
                "version": "1.0",
                "remember": True
            }
        }
    }

    login_response = login_session.post(headers=login_headers,
                                        url=MAIN_URL, json=login_params, verify=False)

    token = login_response.json()["result"]["token"]
    keiro_cookies = login_session.cookies.get_dict()
    return {"token": token, "cookies": keiro_cookies}


def get_current_blacklist():
    credentials = get_credentials()

    get_current_blacklist_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    get_current_blacklist_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "CallerIdBlacklist.get",
    }

    get_current_blacklist_session = requests.Session()
    get_current_blacklist_response = get_current_blacklist_session.post(headers=get_current_blacklist_headers,
                                                                        url=MAIN_URL, json=get_current_blacklist_params,
                                                                        verify=False, cookies=credentials["cookies"])
    return get_current_blacklist_response.json()["result"]


def block_number(number):
    credentials = get_credentials()

    block_number_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    current_blacklist = get_current_blacklist()

    block_number_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "CallerIdBlacklist.set",
        "params": {
            "blockAnonymous": current_blacklist["blockAnonymous"],
            "blacklistItemList": current_blacklist["blacklistItemList"] + [
                {"expression": number, "enabled": True, "description": ""}]
        }
    }

    block_number_session = requests.Session()
    block_number_response = block_number_session.post(
        headers=block_number_headers, url=MAIN_URL, json=block_number_params, verify=False,
        cookies=credentials["cookies"])

    return block_number_response.json()


def hang_up(channel):
    credentials = get_credentials()

    hang_up_headers = {
        "Content-Type": "application/json",
        "X-Token": credentials["token"]
    }

    hang_up_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Server.hangupCall",
        "params": {
            "channels": [
                channel

            ]
        }
    }

    hang_up_session = requests.Session()
    hang_up_request = hang_up_session.post(
        headers=hang_up_headers, json=hang_up_params, url=MAIN_URL, verify=False, cookies=credentials["cookies"])

    print(hang_up_request.json())

    return hang_up_request.json()


def get_calls():
    credentials = get_credentials()
    get_calls_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
        "X-Token": credentials["token"]
    }

    get_calls_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Status.getCalls",
        "params": {
            "query": {
                "limit": -1,
                "start": 0,
                "orderBy": [
                    {
                        "columnName": "ANSWERED_DURATION",
                        "direction": "Asc"
                    }
                ]
            }
        }
    }

    get_calls_session = requests.Session()
    get_calls_request = get_calls_session.post(
        headers=get_calls_headers, json=get_calls_params, url=MAIN_URL, verify=False, cookies=credentials["cookies"])

    return get_calls_request.json()["result"]


def parse_window24(data):
    if not data["calls"]:
        pass
    else:
        for item in data["calls"]:
            id_call = item["id"].split(".")[0]  # add id only number and check record
            number_call = item["FROM"]["NUMBER"]
            status = item["STATUS"]
            call = Call.objects.filter(id_call=id_call)  # if not record call id in db
            if not call:

                try:
                    number = Number.objects.get(number=number_call)
                except Number.DoesNotExist:
                    number = Number.objects.create(number=number_call)

                try:
                    client = Client.objects.get(numbers=number)
                    client_id = client.id
                    client_name = client.name
                except Client.DoesNotExist:
                    client_id = "0"
                    client_name = None


                call = Call(id_call=id_call, number=number, datetime=datetime.datetime.now(),
                            call_type=status, client_id=client_id, client_name=client_name)
                call.save()
            else:
                Call.objects.filter(id_call=id_call).update(call_type=status)



call_reg = []


def parse_okna360(data):
    if not data['calls']:
        pass
    else:
        for item in data['calls']:
            id_call = item["id"].split(".")[0]  # add id only number and check record

            check_call = Call_Okna.objects.filter(id_call=id_call)  # if not record call id in db
            if not check_call:
                call = Call_Okna(id_call=id_call)
                call.save()
                number = item["FROM"]["NUMBER"]
                if not (number == '14') and not (number == '15'):
                    response = requests.post(
                        f'https://okna360-crm.ru/ERPOKNA360/AddNewCalls.php?key=d41d8cd98f00b204e9800998ecf8427e&PhoneClient={number}')


def parse_active_calls():
    data = get_calls()
    parse_okna360(data)
    parse_window24(data)
