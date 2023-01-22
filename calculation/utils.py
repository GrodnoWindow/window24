from constructor.models import Windowsill, LowTides
from .models import *


def calc_window_disc(profile_id, fittings_id, currency, price):
    exchange_rates = ExchangeRates.objects.get(name=currency)
    try:
        window = WindowDiscountMarkups.objects.get(profile_id=profile_id, fittings_id=fittings_id)
        discount = window.discount
        disc_window = (float(price) / 100) * discount  # discount window

        window_input_price = exchange_rates.value * (float(price) - disc_window)  # price in BYN - discount
    except:
        window_input_price = exchange_rates.value * float(price)  # price in BYN
        discount = 0.0

    in_percent = window.markups_in_percent
    markup = window.markups
    if in_percent:
        window_price_with_markup = window_input_price + (window_input_price / 100 * markup)  # + MARKUP
    else:
        window_price_with_markup = window_input_price + markup  # + MARKUP

    window_price_with_markup = round(window_price_with_markup, 2)  # round output price

    window_calc = WindowsCalc.objects.create(discount=discount, price_input=price,
                                             profile_id=profile_id,
                                             fittings_id=fittings_id,
                                             currency_name=exchange_rates.name,
                                             currency_value=exchange_rates.value,
                                             price_output=window_price_with_markup,
                                             markup_percent=in_percent,
                                             markup_value=markup)

    return window_calc


def calc_windowsill(windowsill_id, width, length, count, markups_type):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    windowsill_markups = Windowsill_Markups.objects.get(windowsill=windowsill_id)
    price_input_windowsill = windowsill.price_input

    in_percent = None
    markup = None
    if markups_type == 0:
        in_percent = windowsill_markups.markups_diler_in_percent
        markup = windowsill_markups.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = windowsill_markups.markups_retail_in_percent
        markup = windowsill_markups.markups_retail
        markups_name = 'Розничная'

    if in_percent:
        price_windowsill = price_input_windowsill + (price_input_windowsill / 100 * markup)  # MARKUP
    else:
        price_windowsill = price_input_windowsill + markup  # MARKUP

    sum = price_windowsill * ((width * length) / 1000000)
    if count > 0:
        sum = sum * count
    sum = round(sum, 2)
    windowsill_calc = WindowsillCalc.objects.create(windowsill_id=windowsill.id, width=width, length=length,
                                                    count=count,
                                                    price_output=sum, markups_type=markups_name)

    return windowsill_calc


def calc_low_tides(low_tides_id, width, length, count, markups_type):
    low_tides = LowTides.objects.get(id=low_tides_id)
    low_tides_markup = LowTides_Markups.objects.get(id=low_tides_id)

    price_input_low_tides = low_tides.price_input

    if markups_type == 0:
        in_percent = low_tides_markup.markups_diler_in_percent
        markup = low_tides_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = low_tides_markup.markups_retail_in_percent
        markup = low_tides_markup.markups_retail
        markups_name = 'Розничная'

    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    if count > 0:
        sum = sum * count
    sum = round(sum, 2)
    low_tides_calc = LowTidesCalc.objects.create(low_tides_id=low_tides.id, width=width, length=length,
                                                 count=count,
                                                 price_output=sum, markups_type=markups_name)

    return low_tides_calc
