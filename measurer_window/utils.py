from .models import *


def calc_windowsill(order_id, windowsill_id, width, length, count):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    price_in_byn = windowsill.price_in_byn
    price_in_currency = windowsill.price_in_currency
    width = float(width)
    length = float(length)
    count = int(count)
    sum_byn = price_in_byn * ((width * length) / 1000000)
    sum_currency = price_in_currency * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum_byn = sum_byn * count
        sum_currency = sum_currency * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)
    windowsill_calc = WindowsillCalc.objects.create(order_id=order_id,
                                                    windowsill=windowsill,
                                                    width=width,
                                                    length=length,
                                                    count=count,
                                                    price_in_byn=sum_byn,
                                                    price_in_currency=sum_currency,
                                                    square_meter=square_meter,
                                                    linear_meter=linear_meter)

    return windowsill_calc


def calc_windowsill_complect(order_id, windowsill_id, windowsill_count):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    price_in_byn = windowsill.price_in_byn
    price_in_currency = windowsill.price_in_currency
    count = int(windowsill_count)

    if count > 0:
        sum_byn = price_in_byn * count
        sum_currency = price_in_currency * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    windowsill_calc = WindowsillComplectCalc.objects.create(order_id=order_id,
                                                            windowsill=windowsill,
                                                            count=count,
                                                            price_in_byn=sum_byn,
                                                            price_in_currency=sum_currency)

    return windowsill_calc


def calc_low_tides(order_id, low_tides_id, width, length, count):
    low_tides = LowTides.objects.get(id=low_tides_id)
    price_in_byn = low_tides.price_in_byn
    price_in_currency = low_tides.price_in_currency
    width = float(width)
    length = float(length)
    count = int(count)
    sum_byn = price_in_byn * ((width * length) / 1000000)
    sum_currency = price_in_currency * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum_byn = sum_byn * count
        sum_currency = sum_currency * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)
    low_tides_calc = LowTidesCalc.objects.create(order_id=order_id,
                                                 low_tides=low_tides,
                                                 width=width,
                                                 length=length,
                                                 count=count,
                                                 price_in_byn=sum_byn,
                                                 price_in_currency=sum_currency,
                                                 square_meter=square_meter,
                                                 linear_meter=linear_meter)

    return low_tides_calc


def calc_low_tides_complect(order_id, low_tides, low_tides_count):
    low_tides = LowTides.objects.get(id=low_tides)
    price_in_byn = low_tides.price_in_byn
    price_in_currency = low_tides.price_in_currency
    count = int(low_tides_count)

    if count > 0:
        sum_byn = price_in_byn * count
        sum_currency = price_in_currency * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    low_tides_calc = LowTidesComplectCalc.objects.create(order_id=order_id,
                                                         low_tides=low_tides,
                                                         count=count,
                                                         price_in_byn=sum_byn,
                                                         price_in_currency=sum_currency)

    return low_tides_calc


def calc_order(order_id):
    order = Order.objects.get(pk=order_id)
    sum_byn = 0.0
    sum_currency = 0.0

    windowsill_calc = WindowsillCalc.objects.filter(order_id=order_id)
    for el in windowsill_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    windowsill_complect_calc = WindowsillComplectCalc.objects.filter(order_id=order_id)
    for el in windowsill_complect_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    low_tides_calc = LowTidesCalc.objects.filter(order_id=order_id)
    for el in low_tides_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    low_tides_complect_calc = LowTidesComplectCalc.objects.filter(order_id=order_id)
    for el in low_tides_complect_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    order.sum_in_byn = round(sum_byn, 2)
    order.sum_in_currency = round(sum_currency, 2)
    order.save()
