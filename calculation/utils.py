import math

from constructor.models import Windowsill, LowTides, CasingPrice, CasingNipelPrice, InsternalSlopePrice
from .models import *


def calc_window_disc(profile_id, fittings_id, markup_type, currency, price):
    exchange_rates = ExchangeRates.objects.get(name=currency)
    try:
        window = WindowDiscountMarkups.objects.get(profile_id=profile_id, fittings_id=fittings_id)
        discount = window.discount
        disc_window = (float(price) / 100) * discount  # discount window

        window_input_price = exchange_rates.value * (float(price) - disc_window)  # price in BYN - discount
    except:
        window_input_price = exchange_rates.value * float(price)  # price in BYN
        discount = 0.0

    if markup_type == 0:
        in_percent = window.markups_diler_in_percent
        markup = window.markups_diler
        markups_name = "0"
    elif markup_type == 1:
        in_percent = window.markups_retail_in_percent
        markup = window.markups_retail
        markups_name = "1"
    elif markup_type == 2:
        in_percent = window.markups_3_in_percent
        markup = window.markups_3
        markups_name = '2'
    elif markup_type == 3:
        in_percent = window.markups_4_in_percent
        markup = window.markups_4
        markups_name = '3'
    elif markup_type == 4:
        in_percent = window.markups_5_in_percent
        markup = window.markups_5
        markups_name = '4'
    elif markup_type == 5:
        in_percent = window.markups_6_in_percent
        markup = window.markups_6
        markups_name = '5'
    elif markup_type == 6:
        in_percent = window.markups_7_in_percent
        markup = window.markups_7
        markups_name = '6'

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
                                             markups_type=markup_type,
                                             markups_percent=in_percent,
                                             markups_value=markup,
                                             markups_name=markups_name)

    return window_calc


def calc_windowsill(windowsill_id, installation_id, color_id, width, length, count, markups_type, plug, connector):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    windowsill_markups = WindowsillMarkups.objects.get(windowsill=windowsill_id)
    price_input_windowsill = windowsill.price_input
    in_percent = False
    markup = 0.0
    markups_name = "None"
    if markups_type == 0:
        in_percent = windowsill_markups.markups_diler_in_percent
        markup = windowsill_markups.markups_diler
        markups_name = "0"
    elif markups_type == 1:
        in_percent = windowsill_markups.markups_retail_in_percent
        markup = windowsill_markups.markups_retail
        markups_name = "1"

    elif markups_type == 2:
        in_percent = windowsill_markups.markups_3_in_percent
        markup = windowsill_markups.markups_3
        markups_name = "2"

    elif markups_type == 3:
        in_percent = windowsill_markups.markups_4_in_percent
        markup = windowsill_markups.markups_4
        markups_name = "3"

    elif markups_type == 4:
        in_percent = windowsill_markups.markups_5_in_percent
        markup = windowsill_markups.markups_5
        markups_name = "4"

    if in_percent:
        price_windowsill = price_input_windowsill + (price_input_windowsill / 100 * markup)  # MARKUP
    else:
        price_windowsill = price_input_windowsill + markup  # MARKUP

    width = int(width)
    length = int(length)
    count = int(count)
    plug = int(plug)
    connector = int(connector)

    sum = price_windowsill * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = length / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count
    if plug > 0:
        windowsill_plug_sum = windowsill.windowsill_plug.price_input * plug
        sum = sum + windowsill_plug_sum
    if connector > 0:
        windowsill_connector_sum = windowsill.windowsill_connection.price_input * connector
        sum = sum + windowsill_connector_sum

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    windowsill_calc = WindowsillCalc.objects.create(windowsill_id=windowsill.id, width=width, length=length,
                                                    count=count,
                                                    price_output=sum, markups_type=markups_name,
                                                    square_meter=square_meter,
                                                    linear_meter=linear_meter,
                                                    installation_id=installation_id, color_id=color_id)

    return windowsill_calc


def calc_low_tides(low_tides_id, installation_id, color_id, width, width_1, width_2, width_3, length, count,
                   markups_type, plug, low_tides_type):
    low_tides = LowTides.objects.get(id=low_tides_id)
    low_tides_markup = LowTidesMarkups.objects.get(lowtides=low_tides_id)

    price_input_low_tides = low_tides.price_input

    width = width + width_1 + width_2 + width_3  # + 55 мм
    if markups_type == 0:
        in_percent = low_tides_markup.markups_diler_in_percent
        markup = low_tides_markup.markups_diler
        markups_name = "0"
    elif markups_type == 1:
        in_percent = low_tides_markup.markups_retail_in_percent
        markup = low_tides_markup.markups_retail
        markups_name = "1"

    elif markups_type == 2:
        in_percent = low_tides_markup.markups_3_in_percent
        markup = low_tides_markup.markups_3
        markups_name = "2"

    elif markups_type == 3:
        in_percent = low_tides_markup.markups_4_in_percent
        markup = low_tides_markup.markups_4
        markups_name = "3"

    elif markups_type == 4:
        in_percent = low_tides_markup.markups_5_in_percent
        markup = low_tides_markup.markups_5
        markups_name = "4"

    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = length / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    low_tides_calc = LowTidesCalc.objects.create(low_tides_id=low_tides.id,
                                                 low_tides_type=low_tides_type,
                                                 width=width, width_1=width_1, width_2=width_2, width_3=width_3,
                                                 length=length,
                                                 count=count,
                                                 price_output=sum, markups_type=markups_name, plug=plug,
                                                 square_meter=square_meter,
                                                 linear_meter=linear_meter,
                                                 installation_id=installation_id, color_id=color_id)

    return low_tides_calc


def calc_flashing(flashing_id, installation_id, color_id, width, length, count, markups_type):
    flashing = Flashing.objects.get(id=flashing_id)

    flashing_markup = FlashingMarkups.objects.get(flashing=flashing)

    price_input_flashing = flashing.price_input

    # print(price_input_flashing)
    # print(markups_type)
    if markups_type == 0:
        in_percent = flashing_markup.markups_diler_in_percent
        markup = flashing_markup.markups_diler
        markups_name = '0'
    elif markups_type == 1:
        in_percent = flashing_markup.markups_retail_in_percent
        markup = flashing_markup.markups_retail
        markups_name = '1'
    elif markups_type == 2:
        in_percent = flashing_markup.markups_3_in_percent
        markup = flashing_markup.markups_3
        markups_name = '2'

    elif markups_type == 3:
        in_percent = flashing_markup.markups_4_in_percent
        markup = flashing_markup.markups_4
        markups_name = '3'

    elif markups_type == 4:
        in_percent = flashing_markup.markups_5_in_percent
        markup = flashing_markup.markups_5
        markups_name = '4'

    if in_percent:
        price_input_flashing = price_input_flashing + (price_input_flashing / 100 * markup)
    else:
        price_input_flashing = price_input_flashing + markup

    if flashing.type == 0:  # metal -> m2
        sum = price_input_flashing * (((width + 30) * length) / 1000000)
    elif flashing.type == 1:
        width = flashing.width
        sum = price_input_flashing * (length / 1000)
    # print(price_input_flashing)
    square_meter = (width * length) / 1000
    linear_meter = length / 1000
    # print(linear_meter)
    # print(square_meter)
    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    flahsing_calc = FlashingCalc.objects.create(flashing_id=flashing.id, width=width, length=length,
                                                count=count,
                                                price_output=sum, markups_type=markups_name,
                                                square_meter=square_meter,
                                                linear_meter=linear_meter,
                                                installation_id=installation_id, color_id=color_id)

    return flahsing_calc


def calc_casing(casing_id, installation_id, color_id, fastening_id, width, length, count, markups_type):
    casing = Casing.objects.get(id=casing_id)
    casing_markup = CasingMarkups.objects.get(casing=casing_id)

    casing_price = CasingPrice.objects.get(casing=casing, width=width)
    price_input_casing = casing_price.price_input

    if markups_type == 0:
        in_percent = casing_markup.markups_diler_in_percent
        markup = casing_markup.markups_diler
        markups_name = '0'
    elif markups_type == 1:
        in_percent = casing_markup.markups_retail_in_percent
        markup = casing_markup.markups_retail
        markups_name = '1'
    elif markups_type == 2:
        in_percent = casing_markup.markups_3_in_percent
        markup = casing_markup.markups_3
        markups_name = '2'
    elif markups_type == 3:
        in_percent = casing_markup.markups_4_in_percent
        markup = casing_markup.markups_4
        markups_name = '3'
    elif markups_type == 4:
        in_percent = casing_markup.markups_5_in_percent
        markup = casing_markup.markups_5
        markups_name = '4'
    # print(price_input_casing)

    if in_percent:
        price_input_casing = price_input_casing + (price_input_casing / 100 * markup)
    else:
        price_input_casing = price_input_casing + markup
    # print(price_input_casing)
    sum = price_input_casing * (length / 1000)
    # print(sum)
    square_meter = (width * length) / 1000000
    linear_meter = length / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    # + nipels

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    nipel = CasingNipelPrice.objects.get(casing=casing)

    nipel.price_input
    nipel_count = int(linear_meter) * 5

    price_nipel = (nipel_count * nipel.price_input)
    print(sum)
    print(price_nipel)
    sum = sum + price_nipel
    sum = round(sum, 2)
    casing_calc = CasingCalc.objects.create(casing_id=casing_id, width=width, length=length,
                                            count=count,
                                            price_output=sum, markups_type=markups_name,
                                            square_meter=square_meter,
                                            nipel_count=nipel_count,
                                            fastening_id=fastening_id,
                                            linear_meter=linear_meter,
                                            installation_id=installation_id, color_id=color_id)

    return casing_calc


def calc_visors(visors_id, installation_id, color_id, width_1, width_2, width_3, length, count, markups_type):
    width = width_1 + width_2 + width_3 + 50
    visors = Visors.objects.get(id=visors_id)
    visors_markup = VisorsMarkups.objects.get(visors=visors_id)

    price_input_low_tides = visors.price_input

    if markups_type == 0:
        in_percent = visors_markup.markups_diler_in_percent
        markup = visors_markup.markups_diler
        markups_name = '0'
    elif markups_type == 1:
        in_percent = visors_markup.markups_retail_in_percent
        markup = visors_markup.markups_retail
        markups_name = '1'
    elif markups_type == 2:
        in_percent = visors_markup.markups_3_in_percent
        markup = visors_markup.markups_3
        markups_name = '2'
    elif markups_type == 3:
        in_percent = visors_markup.markups_4_in_percent
        markup = visors_markup.markups_4
        markups_name = '3'
    elif markups_type == 4:
        in_percent = visors_markup.markups_5_in_percent
        markup = visors_markup.markups_5
        markups_name = '4'
    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = length / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    visors_calc = VisorsCalc.objects.create(visors_id=visors_id, width=width, length=length,
                                            count=count, width_1=width_1, width_2=width_2, width_3=width_3,
                                            price_output=sum, markups_type=markups_name,
                                            square_meter=square_meter,
                                            linear_meter=linear_meter,
                                            installation_id=installation_id, color_id=color_id)

    return visors_calc


def calc_slopes_of_metal(slopes_of_metal_id, installation_id, color_id,
                         width_1, width_2, width_3, width_4,
                         lock_width_1, lock_width_2, lock_width_3, lock_width_4,lock_length,
                         low_tides_width_1, low_tides_width_2, low_tides_width_3, low_tides_width_4,low_tides_length,
                         length, count, markups_type):
    slopes_of_metal = SlopesOfMetal.objects.get(id=slopes_of_metal_id)
    slopes_of_metal_markup = SlopesOfMetalMarkups.objects.get(slopes_of_metal=slopes_of_metal)
    lock_price = slopes_of_metal.slopes_of_metal_lock.price_input
    low_tides_price = slopes_of_metal.slopes_of_metal_low_tides.price_input
    price_input = slopes_of_metal.price_input
    width = width_1 + width_2 + width_3 + width_4
    low_tides_width = low_tides_width_1 + low_tides_width_2 + low_tides_width_3 + low_tides_width_4
    lock_width = lock_width_1 + lock_width_2 + lock_width_3 + lock_width_4

    if markups_type == 0:
        in_percent = slopes_of_metal_markup.markups_diler_in_percent
        markup = slopes_of_metal_markup.markups_diler
        markups_name = '0'
    elif markups_type == 1:
        in_percent = slopes_of_metal_markup.markups_retail_in_percent
        markup = slopes_of_metal_markup.markups_retail
        markups_name = '1'
    elif markups_type == 2:
        in_percent = slopes_of_metal_markup.markups_3_in_percent
        markup = slopes_of_metal_markup.markups_3
        markups_name = '2'
    elif markups_type == 3:
        in_percent = slopes_of_metal_markup.markups_4_in_percent
        markup = slopes_of_metal_markup.markups_4
        markups_name = '3'
    elif markups_type == 4:
        in_percent = slopes_of_metal_markup.markups_5_in_percent
        markup = slopes_of_metal_markup.markups_5
        markups_name = '4'

    if in_percent:
        price = price_input + (price_input / 100 * markup)
    else:
        price = price_input + markup

    sum_lock = lock_price * ((lock_width * lock_length) / 1000000)
    try:
        sum_low_tides = low_tides_price * ((low_tides_width * low_tides_length) / 1000000)
    except:
        sum_low_tides = 0

    sum = price * ((width * length) / 1000000)

    sum = sum + sum_lock + sum_low_tides

    square_meter = (width * length) / 1000000
    linear_meter = length / 1000

    square_meter_lock = (lock_width * lock_length) / 1000000
    linear_meter_lock = lock_length / 1000

    square_meter_low_tides = (low_tides_width * low_tides_length) / 1000000
    linear_meter_low_tides = low_tides_length / 1000

    lock_count = math.ceil((lock_width * length) / 1000000)

    if count > 0:
        sum_lock = sum_lock * count
        sum_low_tides = sum_low_tides * count
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

        square_meter_lock = square_meter_lock * count
        linear_meter_lock = linear_meter_lock * count

        square_meter_low_tides = square_meter_low_tides * count
        linear_meter_low_tides = linear_meter_low_tides * count

    sum_low_tides = round(sum_low_tides, 2)
    sum_lock = round(sum_lock, 2)
    sum = round(sum, 2)

    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    square_meter_lock = round(square_meter_lock, 2)
    linear_meter_lock = round(linear_meter_lock, 2)

    square_meter_low_tides = round(square_meter_low_tides, 2)
    linear_meter_low_tides = round(linear_meter_low_tides, 2)

    slopes_of_metal_calc = SlopesOfMetalCalc.objects.create(slopes_of_metal_id=slopes_of_metal.id, width=width,
                                                            width_1=width_1,
                                                            width_2=width_2,
                                                            width_3=width_3,
                                                            width_4=width_4,
                                                            lock_width=lock_width,
                                                            price_lock=sum_lock,
                                                            price_low_tides=sum_low_tides,
                                                            lock_width_1=lock_width_1,
                                                            lock_width_2=lock_width_2,
                                                            lock_width_3=lock_width_3,
                                                            lock_width_4=lock_width_4,
                                                            square_meter_lock=square_meter_lock,
                                                            linear_meter_lock=linear_meter_lock,
                                                            low_tides_width=low_tides_width,
                                                            square_meter_low_tides=square_meter_low_tides,
                                                            linear_meter_low_tides=linear_meter_low_tides,
                                                            low_tides_width_1=low_tides_width_1,
                                                            low_tides_width_2=low_tides_width_2,
                                                            low_tides_width_3=low_tides_width_3,
                                                            low_tides_width_4=low_tides_width_1,
                                                            lock_count=lock_count,
                                                            length=length,
                                                            count=count,
                                                            price_output=sum, markups_type=markups_name,
                                                            square_meter=square_meter,
                                                            linear_meter=linear_meter,
                                                            installation_id=installation_id, color_id=color_id)

    return slopes_of_metal_calc


def calc_internal_slope(internal_slope_id, installation_id, color_id, type, f_count, height_1, height_2, width, length,
                        count, markups_type):
    internal_slope = InternalSlope.objects.get(id=internal_slope_id)

    internal_slope_markup = InternalSlopeMarkups.objects.get(internal_slope=internal_slope)

    price_input = 0
    if type == 0:  # Кюнель
        try:
            internal_slope_price = InsternalSlopePrice.objects.get(internal_slope=internal_slope, width=width)
            internal_slope_start_profile_price = internal_slope.internal_slope_start_profile.price_input
            internal_slope_casing_price = internal_slope.internal_slope_casing.price_input
            internal_slope_lid_price = internal_slope.internal_slope_lid.price_input
            internal_slope_latch_price = internal_slope.internal_slope_latch.price_input
            price_input = internal_slope_price.price_input
        except:
            pass
    elif type == 1:  # F
        internal_slope_f_price = internal_slope.internal_slope_f.price_input

        price_input = internal_slope.price_input
    print(price_input)
    if markups_type == 0:
        in_percent = internal_slope_markup.markups_diler_in_percent
        markup = internal_slope_markup.markups_diler
        markups_name = '0'
    elif markups_type == 1:
        in_percent = internal_slope_markup.markups_retail_in_percent
        markup = internal_slope_markup.markups_retail
        markups_name = '1'
    elif markups_type == 2:
        in_percent = internal_slope_markup.markups_3_in_percent
        markup = internal_slope_markup.markups_3
        markups_name = '2'
    elif markups_type == 3:
        in_percent = internal_slope_markup.markups_4_in_percent
        markup = internal_slope_markup.markups_4
        markups_name = '3'
    elif markups_type == 4:
        in_percent = internal_slope_markup.markups_5_in_percent
        markup = internal_slope_markup.markups_5
        markups_name = '4'

    if in_percent:
        price = price_input + (price_input / 100 * markup)
    else:
        price = price_input + markup
    square_meter = (length + height_1 + height_2) * width / 1000000
    linear_meter = (length + height_1 + height_2) / 1000

    print(square_meter)
    print(price)
    if type == 0:
        sum = price * linear_meter
    elif type == 1:
        sum = price * square_meter
    print(sum)
    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    lid_count = 0
    if type == 0:  # Кюнель
        try:
            count_latch = math.ceil(linear_meter) * 4
            sum += linear_meter * internal_slope_start_profile_price  # + старт профиль
            sum += linear_meter * internal_slope_casing_price  # + наличник
            sum += count_latch * internal_slope_latch_price  # + защелка
            sum = sum + (internal_slope_lid_price * 2)  # + 2 крышки
            lid_count = 2
        except:
            pass

    elif type == 1:  # F

        sum += f_count * internal_slope_f_price  # + F профиль
        count_latch = 0
        lid_count = 0

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    internal_slop_calc = InternalSlopeCalc.objects.create(internal_slope_id=internal_slope.id, width=width,
                                                          length=length,
                                                          count=count,
                                                          lid_count=lid_count,
                                                          latch_count=count_latch,
                                                          f_count=f_count,
                                                          height_1=height_1,
                                                          height_2=height_2,
                                                          start_profile_length=linear_meter,
                                                          casing_length=linear_meter,
                                                          price_output=sum, markups_type=markups_name,
                                                          square_meter=square_meter,
                                                          linear_meter=linear_meter,
                                                          installation_id=installation_id, color_id=color_id)

    return internal_slop_calc
