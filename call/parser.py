import requests
import time


API_URL = "https://86.57.178.104:4021"
MAIN_URL = API_URL + "/admin/api/jsonrpc/"
LOGIN = "Ilya"
PASSWORD = "bkmz1337"


def parse():
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

    fetch_phones_headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.61 Safari/537.36",
        "X-Token": token
    }

    fetch_phones_params = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "CallHistory.get",
        "params": {
            "query": {
                "limit": 100,
                "start": 0,
                "orderBy": [
                    {
                        "columnName": "TIMESTAMP",
                        "direction": "Desc"
                    }
                ]
            }
        }
    }

    fetch_phones_session = requests.Session()

    while True:
        fetch_phones_request = fetch_phones_session.post(
            headers=fetch_phones_headers, json=fetch_phones_params, url=MAIN_URL, verify=False, cookies=keiro_cookies)
        print(fetch_phones_request.json())
        time.sleep(10)


if __name__ == "__main__":
    parse()