import datetime

import requests,csv

from .models import Call
from client.models import Client


API_URL = "https://86.57.178.104:4021"
# API_URL = "https://192.168.1.209:4021"
MAIN_URL = API_URL + "/admin/api/jsonrpc/"
LOGIN = "Ilya"
PASSWORD = "bkmz1337"


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


def parse_active_calls():
    data = get_calls()
    print(data)
    if data["calls"] == []:
        print('No call for record')
        return False
    else:
        print('zashel')
        for item in data["calls"]:
            id_call = item["id"].split(".")[0] # add id only number and check record
            check_call = Call.objects.filter(id_call=id_call) # if not record call id in db
            if not check_call:
                number = item["FROM"]["NUMBER"]
                status = item["STATUS"]
                check_client = Client.objects.filter(number=number).values("id")
                if not check_client:
                    client_id = "0"
                    client_name = "new client"
                else:
                    client_id = check_client
                    client_name = Client.objects.filter(number=number).values("name")
                    print(client_name)
                    print(client_id)

                call = Call(id_call=id_call, number=number, status=status,datetime=datetime.datetime.now(),
                            id_client=client_id, name_client=client_name)

                call.save()
                print('SAVE')
                return True



def database_reader():
    with open('call-history.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            if not(row['From Number'] == "14") and not(row['From Number'] == "15"):
                call = Call(number=row['From Number'], datetime=row['Time'])
                call.save()
                i += 1
                print(f'complete : {i}')
        print('complete')

    csvfile.close()
# 3.72
