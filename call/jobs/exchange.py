from calculation.models import ExchangeRates, WindowDiscount
import requests
from bs4 import BeautifulSoup


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
            try:
                exchange_rate = ExchangeRates.objects.get(name='USD')
                exchange_rate.value = temp
                exchange_rate.save()
            except ExchangeRates.DoesNotExist:
                ExchangeRates.objects.create(name='USD', value=temp)
        elif row[0] == 'Российский рубль':
            temp = temp / 100
            try:
                exchange_rate = ExchangeRates.objects.get(name='RUB')
                exchange_rate.value = temp
                exchange_rate.save()
            except ExchangeRates.DoesNotExist:
                ExchangeRates.objects.create(name='RUB', value=temp)
        elif row[0] == 'Евро':
            try:
                exchange_rate = ExchangeRates.objects.get(name='EUR')
                exchange_rate.value = temp
                exchange_rate.save()
            except ExchangeRates.DoesNotExist:
                ExchangeRates.objects.create(name='EUR', value=temp)
