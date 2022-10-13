# from .models import WindowDiscount, ExchangeRates
from calculation.models import ExchangeRates, WindowDiscount
import requests
from bs4 import BeautifulSoup
import lxml


def parse_exchange_rates():
    url = 'https://www.nbrb.by/statistics/rates/ratesdaily.asp'
    try:
        response = requests.get(url)
    except:
        pass
    soup = BeautifulSoup(response.text, 'lxml')
    data = []
    table = soup.find('table', attrs={'class': 'currencyTable'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    for row in data:
        temp = float(row[2].replace(',', '.'))
        if row[0] == 'Доллар США':
            ExchangeRates.objects.filter(name='USD').update(value=temp)
        elif row[0] == 'Российский рубль':
            temp = temp / 100
            ExchangeRates.objects.filter(name='RUB').update(value=temp)
        elif row[0] == 'Евро':
            ExchangeRates.objects.filter(name='EUR').update(value=temp)


def calc_window_disc(profile_id, fittings_id, currency, price):
    parse_exchange_rates()

    discount = WindowDiscount.objects.get(profile_id=profile_id, fittings_id=fittings_id).discount
    print(f"disc {discount}")

    disc_window = (float(price) / 100) * discount
    exchange_rub = ExchangeRates.objects.get(name=currency).value

    sum = exchange_rub * (float(price) - disc_window)
    print(f'profile: {profile_id} and fittings {fittings_id} ')

    print(f'цена окна {price} {currency}')
    print(f'скидка на окно {discount}% = {disc_window}')
    print(f'сумма - скидка = {float(price) - disc_window}')
    print(f' {float(price) - disc_window} {currency} сумма в {sum} BYN')

    return sum


