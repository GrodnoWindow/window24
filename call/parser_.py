import requests, json
import time
from .models import Call
from datetime import datetime


API_URL = "https://86.57.178.104:4021"
MAIN_URL = API_URL + "/admin/api/jsonrpc/"
LOGIN = "Ilya"
PASSWORD = "bkmz1337"
bkmz1337

def parse_active_call():
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
                "vendor": "Kerio",
                "version": "1.0",
                "remember": True
            }
        }
    }

    login_response = login_session.post(headers=login_headers,
                                        url=MAIN_URL, json=login_params, verify=False)

    token = login_response.json()["result"]["token"]
    keiro_cookies = login_session.cookies.get_dict()

    fetch_phones_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
        "X-Token": token
    }

    fetch_phones_params = {
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

    fetch_phones_session = requests.Session()

    fetch_phones_request = fetch_phones_session.post(
        headers=fetch_phones_headers, json=fetch_phones_params, url=MAIN_URL, verify=False, cookies=keiro_cookies)
    data = fetch_phones_request.json()
    # print(data)
    if not data["result"]["calls"]:
        print('None')
        return None
    else:
        for item in data["result"]["calls"]:
            if item["TO"]["NUMBER"] == "14":
                id_call = item["id"]
                number = item["FROM"]["NUMBER"]
                status = "Не принят"
                client = "Новый клиент"
                call = Call(id_call=id_call,number=number,status=status,client=client)
                call.save()



if __name__ == "__main__":
    pass
    # parse()
