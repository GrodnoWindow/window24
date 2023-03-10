from .models import *


def calc_windowsill(order_id, windowsill, windowsill_color, windowsill_width, windowsill_count, windowsill_plug,
                    windowsill_plug_count,
                    windowsill_connection, windowsill_connection_count, length):
    sum_byn = 0.0
    sum_currency = 0.0
    if (windowsill_count is None) or (windowsill_count == 0) or (windowsill_width is None):
        return

    # if not(windowsill_plug is None) and (int(windowsill_plug_count) > 0):
    sum_plug_byn = windowsill_plug.price_in_byn * windowsill_plug_count
    sum_plug_currency = windowsill_plug.price_in_currency * windowsill_plug_count
# else:
    sum_plug_byn = 0.0
    sum_plug_currency = 0.0

    if not (windowsill_connection is None) and (windowsill_connection_count > 0):
        sum_connection_byn = windowsill_connection.price_in_byn * windowsill_connection_count
        sum_connection_currency = windowsill_connection.price_in_currency * windowsill_connection_count
    else:
        sum_connection_byn = 0.0
        sum_connection_currency = 0.0

    if windowsill_count > 0 and not(windowsill_width is None) and not(length is None):
        sum_windowsill_byn = (windowsill.price_in_byn * (
                    (float(windowsill_width.name) * length) / 1000000)) * windowsill_count
        sum_windowsill_currency = (windowsill.price_in_currency * (
                    (float(windowsill_width.name) * length) / 1000000)) * windowsill_count
        square_meter = ((float(windowsill_width.name) * length) / 1000000) * windowsill_count
        linear_meter = (length / 1000) * windowsill_count
        sum_windowsill_byn = sum_windowsill_byn * windowsill_count
        sum_windowsill_currency = sum_windowsill_currency * windowsill_count
    else:
        sum_windowsill_byn = 0.0
        sum_windowsill_currency = 0.0
        linear_meter = 0
        square_meter = 0
    sum_byn = sum_windowsill_byn + sum_plug_byn + sum_connection_byn
    sum_currency = sum_windowsill_currency + sum_plug_currency + sum_connection_currency
    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)
    windowsill_calc = WindowsillCalc.objects.create(order_id=order_id,
                                                    windowsill=windowsill,
                                                    windowsill_color=windowsill_color,
                                                    windowsill_width=windowsill_width,
                                                    windowsill_count=windowsill_count,
                                                    windowsill_plug=windowsill_plug,
                                                    sum_plug_byn=sum_plug_byn,
                                                    sum_plug_currency=sum_plug_currency,
                                                    sum_windowsill_byn=sum_windowsill_byn,
                                                    sum_windowsill_currency=sum_windowsill_currency,
                                                    sum_connection_byn=sum_connection_currency,
                                                    sum_connection_currency=sum_connection_currency,
                                                    windowsill_plug_count=windowsill_plug_count,
                                                    windowsill_connection=windowsill_connection,
                                                    windowsill_connection_count=windowsill_connection_count,
                                                    length=length,
                                                    square_meter=square_meter,
                                                    linear_meter=linear_meter,
                                                    sum_in_byn=sum_byn,
                                                    sum_in_currency=sum_currency)

    return windowsill_calc


def calc_windowsill_complect(order_id, windowsill, count):
    price_in_byn = windowsill.price_in_byn
    price_in_currency = windowsill.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
    count = int(count)

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


def calc_low_tides(order_id, low_tides, width, length, count):
    price_in_byn = low_tides.price_in_byn
    price_in_currency = low_tides.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
    width = float(width)
    width = width + 55.0  # + 55 мм
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


def calc_low_tides_complect(order_id, low_tides, count):
    price_in_byn = low_tides.price_in_byn
    price_in_currency = low_tides.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
    count = int(count)

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


def calc_visors(order_id, visors, width, length, count):
    price_in_byn = visors.price_in_byn
    price_in_currency = visors.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
    width = float(width)
    width = width + 55.0  # + 55 мм
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
    visors_calc = VisorsCalc.objects.create(order_id=order_id,
                                            visors=visors,
                                            width=width,
                                            length=length,
                                            count=count,
                                            price_in_byn=sum_byn,
                                            price_in_currency=sum_currency,
                                            square_meter=square_meter,
                                            linear_meter=linear_meter)

    return visors_calc


def calc_flashing(order_id, flashing, width, length, count):
    price_in_byn = flashing.price_in_byn
    price_in_currency = flashing.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
    width = float(width)
    width = width + 55.0  # + 55 мм
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
    flashing_calc = FlashingCalc.objects.create(order_id=order_id,
                                                flashing=flashing,
                                                width=width,
                                                length=length,
                                                count=count,
                                                price_in_byn=sum_byn,
                                                price_in_currency=sum_currency,
                                                square_meter=square_meter,
                                                linear_meter=linear_meter)

    return flashing_calc


def calc_casing(order_id, casing, width, length, count):
    price_in_byn = casing.price_in_byn
    price_in_currency = casing.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
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
    casing_calc = CasingCalc.objects.create(order_id=order_id,
                                            casing=casing,
                                            width=width,
                                            length=length,
                                            count=count,
                                            price_in_byn=sum_byn,
                                            price_in_currency=sum_currency,
                                            square_meter=square_meter,
                                            linear_meter=linear_meter)

    return casing_calc


def calc_slopes_of_metal(order_id, slopes_of_metal, width, length, count):
    price_in_byn = slopes_of_metal.price_in_byn
    price_in_currency = slopes_of_metal.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
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
    slopes_of_metal_calc = SlopesOfMetalCalc.objects.create(order_id=order_id,
                                                            slopes_of_metal=slopes_of_metal,
                                                            width=width,
                                                            length=length,
                                                            count=count,
                                                            price_in_byn=sum_byn,
                                                            price_in_currency=sum_currency,
                                                            square_meter=square_meter,
                                                            linear_meter=linear_meter)

    return slopes_of_metal_calc


def calc_internal_slopes(order_id, internal_slopes, width, length, count):
    price_in_byn = internal_slopes.price_in_byn
    price_in_currency = internal_slopes.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0
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
    internal_slopes_calc = InternalSlopesCalc.objects.create(order_id=order_id,
                                                             internal_slopes=internal_slopes,
                                                             width=width,
                                                             length=length,
                                                             count=count,
                                                             price_in_byn=sum_byn,
                                                             price_in_currency=sum_currency,
                                                             square_meter=square_meter,
                                                             linear_meter=linear_meter)

    return internal_slopes_calc


def calc_mounting_materials(order_id, mounting_materials, count):
    price_in_byn = mounting_materials.price_in_byn
    price_in_currency = mounting_materials.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0

    count = int(count)
    sum_byn = price_in_byn
    sum_currency = price_in_currency

    if count > 0:
        sum_byn = sum_byn * count
        sum_currency = sum_currency * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    mounting_materials_calc = MountingMaterialsCalc.objects.create(order_id=order_id,
                                                                   mounting_materials=mounting_materials,
                                                                   count=count,
                                                                   price_in_byn=sum_byn,
                                                                   price_in_currency=sum_currency)

    return mounting_materials_calc


def calc_works(order_id, works, count):
    price_in_byn = works.price_in_byn
    price_in_currency = works.price_in_currency
    if price_in_currency is None:
        price_in_currency = 0.0

    count = int(count)
    sum_byn = price_in_byn
    sum_currency = price_in_currency

    if count > 0:
        sum_byn = sum_byn * count
        sum_currency = sum_currency * count

    sum_byn = round(sum_byn, 2)
    sum_currency = round(sum_currency, 2)

    works_calc = WorksCalc.objects.create(order_id=order_id,
                                          works=works,
                                          count=count,
                                          price_in_byn=sum_byn,
                                          price_in_currency=sum_currency)

    return works_calc


def calc_materials(order):
    sum_byn = 0.0
    sum_currency = 0.0

    windowsill_calc = WindowsillCalc.objects.filter(order_id=order.pk)
    for el in windowsill_calc:
        sum_byn = sum_byn + el.sum_in_byn
        sum_currency = sum_currency + el.sum_in_currency

    windowsill_complect_calc = WindowsillComplectCalc.objects.filter(order_id=order.pk)
    for el in windowsill_complect_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    low_tides_calc = LowTidesCalc.objects.filter(order_id=order.pk)
    for el in low_tides_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    low_tides_complect_calc = LowTidesComplectCalc.objects.filter(order_id=order.pk)
    for el in low_tides_complect_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    visors_calc = VisorsCalc.objects.filter(order_id=order.pk)
    for el in visors_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    flashing_calc = FlashingCalc.objects.filter(order_id=order.pk)
    for el in flashing_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    casing_calc = CasingCalc.objects.filter(order_id=order.pk)
    for el in casing_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    slopes_of_metal_calc = SlopesOfMetalCalc.objects.filter(order_id=order.pk)
    for el in slopes_of_metal_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    internal_slopes_calc = InternalSlopesCalc.objects.filter(order_id=order.pk)
    for el in internal_slopes_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    mounting_materials_calc = MountingMaterialsCalc.objects.filter(order_id=order.pk)
    for el in mounting_materials_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    order.sum_materials_byn = round(sum_byn, 2)
    order.sum_materials_currency = round(sum_currency, 2)


def calc_order_works(order):
    sum_byn = 0.0
    sum_currency = 0.0

    works_calc = WorksCalc.objects.filter(order_id=order.pk)
    for el in works_calc:
        sum_byn = sum_byn + el.price_in_byn
        sum_currency = sum_currency + el.price_in_currency

    order.sum_works_byn = round(sum_byn, 2)
    order.sum_works_currency = round(sum_currency, 2)
    order.save()


def calc_order(order_id):
    order = Order.objects.get(pk=order_id)

    calc_materials(order)
    calc_order_works(order)

    order.sum_byn = round(order.sum_materials_byn + order.sum_works_byn, 2)
    order.sum_currency = round(order.sum_materials_currency + order.sum_works_currency, 2)
    order.save()
