# from .models import WindowDiscount, ExchangeRates
from calculation.models import ExchangeRates, WindowDiscount
import requests
from bs4 import BeautifulSoup
import lxml
from constructor.models import Windowsill, LowTides
from .models import *


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

    disc_window = (float(price) / 100) * discount
    exchange_rub = ExchangeRates.objects.get(name=currency).value

    sum = exchange_rub * (float(price) - disc_window)
    # print(f'profile: {profile_id} and fittings {fittings_id} ')
    #
    # print(f'цена окна {price} {currency}')
    # print(f'скидка на окно {discount}% = {disc_window}')
    # print(f'сумма - скидка = {float(price) - disc_window}')
    # print(f' {float(price) - disc_window} {currency} сумма в {sum} BYN')

    return sum


def calc_windowsill(windowsill_id, width, length, count):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    price_input_windowsill = windowsill.price_input
    # TO DO
    # взять тип подоконника и сделать наценку по типу !!!!
    markup = Markups.objects.last().windowsill

    price_windowsill = price_input_windowsill + (price_input_windowsill / 100 * markup)

    sum = price_windowsill * ((width * length) / 1000000)
    if count > 0:
        sum = sum * count
    sum = round(sum, 2)
    windowsill_calc = WindowsillCalc.objects.create(windowsill_id=windowsill, width=width, length=length,
                                                    count=count,
                                                    price_output=sum)

    return windowsill_calc


def calc_low_tides(low_tides_id, width, length, count):
    low_tides = LowTides.objects.get(id=low_tides_id)
    price_input_low_tides = low_tides.price_input

    markup = Markups.objects.last().low_tides

    price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)

    sum = price_low_tides * ((width * length) / 1000000)
    if count > 0:
        sum = sum * count
    sum = round(sum, 2)
    low_tides_calc = LowTidesCalc.objects.create(low_tides=low_tides, width=width, length=length,
                                                 count=count,
                                                 price_output=sum)

    return low_tides_calc
