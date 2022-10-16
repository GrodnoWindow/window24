from constructor.models import Windowsill, LowTides
from .models import *


def calc_window_disc(profile_id, fittings_id, currency, price):

    exchange_rates = ExchangeRates.objects.get(name=currency)
    try:
        window_discount = WindowDiscount.objects.get(profile_id=profile_id, fittings_id=fittings_id)
        discount = window_discount.value
        disc_window = (float(price) / 100) * discount  # discount window

        window = exchange_rates.value * (float(price) - disc_window)  # price in BYN - discount
    except:
        window = exchange_rates.value * float(price)  # price in BYN
        discount = 0.0

    markup = Markups.objects.last().window
    window_price_with_markup = window + (window / 100 * markup)  # + MARKUP
    window_price_with_markup = round(window_price_with_markup, 2)  # round output price

    window_calc = WindowsCalc.objects.create(discount=discount, price_input=price,
                                             currency_name=exchange_rates.name,
                                             currency_value=exchange_rates.value,
                                             price_output=window_price_with_markup)

    return window_calc


def calc_windowsill(windowsill_id, width, length, count):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    price_input_windowsill = windowsill.price_input
    # TO DO
    # взять тип подоконника и сделать наценку по типу !!!!
    markup = Markups.objects.last().windowsill

    price_windowsill = price_input_windowsill + (price_input_windowsill / 100 * markup)  # <MARKUP

    sum = price_windowsill * ((width * length) / 1000000)
    if count > 0:
        sum = sum * count
    sum = round(sum, 2)
    windowsill_calc = WindowsillCalc.objects.create(windowsill_id=windowsill.id, width=width, length=length,
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
    low_tides_calc = LowTidesCalc.objects.create(low_tides_id=low_tides.id, width=width, length=length,
                                                 count=count,
                                                 price_output=sum)

    return low_tides_calc
