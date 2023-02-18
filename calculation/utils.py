from constructor.models import Windowsill, LowTides
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
        markups_name = 'Диллерская'
    elif markup_type == 1:
        in_percent = window.markups_retail_in_percent
        markup = window.markups_retail
        markups_name = 'Розничная'
    elif markup_type == 2:
        in_percent = window.markups_3_in_percent
        markup = window.markups_3
        markups_name = 'Наценка №3'
    elif markup_type == 3:
        in_percent = window.markups_4_in_percent
        markup = window.markups_4
        markups_name = 'Наценка №4'
    elif markup_type == 4:
        in_percent = window.markups_5_in_percent
        markup = window.markups_5
        markups_name = 'Наценка №5'

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


def calc_windowsill(windowsill_id, width, length, count, markups_type):
    windowsill = Windowsill.objects.get(id=windowsill_id)
    windowsill_markups = WindowsillMarkups.objects.get(windowsill=windowsill_id)
    price_input_windowsill = windowsill.price_input
    in_percent = False
    markup = 0.0
    if markups_type == 0:
        in_percent = windowsill_markups.markups_diler_in_percent
        markup = windowsill_markups.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = windowsill_markups.markups_retail_in_percent
        markup = windowsill_markups.markups_retail
        markups_name = 'Розничная'

    elif markups_type == 2:
        in_percent = windowsill_markups.markups_3_in_percent
        markup = windowsill_markups.markups_3
        markups_name = 'Наценка №3'

    elif markups_type == 3:
        in_percent = windowsill_markups.markups_4_in_percent
        markup = windowsill_markups.markups_4
        markups_name = 'Наценка №4'

    elif markups_type == 4:
        in_percent = windowsill_markups.markups_5_in_percent
        markup = windowsill_markups.markups_5
        markups_name = 'Наценка №5'

    if in_percent:
        price_windowsill = price_input_windowsill + (price_input_windowsill / 100 * markup)  # MARKUP
    else:
        price_windowsill = price_input_windowsill + markup  # MARKUP

    sum = price_windowsill * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    windowsill_calc = WindowsillCalc.objects.create(windowsill_id=windowsill.id, width=width, length=length,
                                                    count=count,
                                                    price_output=sum, markups_type=markups_name,
                                                    square_meter=square_meter,
                                                    linear_meter=linear_meter)

    return windowsill_calc


def calc_low_tides(low_tides_id, width, length, count, markups_type,plug):
    low_tides = LowTides.objects.get(id=low_tides_id)
    low_tides_markup = LowTidesMarkups.objects.get(lowtides=low_tides_id)

    price_input_low_tides = low_tides.price_input

    width = width + 55  # + 55 мм
    if markups_type == 0:
        in_percent = low_tides_markup.markups_diler_in_percent
        markup = low_tides_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = low_tides_markup.markups_retail_in_percent
        markup = low_tides_markup.markups_retail
        markups_name = 'Розничная'

    elif markups_type == 2:
        in_percent = low_tides_markup.markups_3_in_percent
        markup = low_tides_markup.markups_3
        markups_name = 'Наценка №3'

    elif markups_type == 3:
        in_percent = low_tides_markup.markups_4_in_percent
        markup = low_tides_markup.markups_4
        markups_name = 'Наценка №4'

    elif markups_type == 4:
        in_percent = low_tides_markup.markups_5_in_percent
        markup = low_tides_markup.markups_5
        markups_name = 'Наценка №5'

    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    low_tides_calc = LowTidesCalc.objects.create(low_tides_id=low_tides.id, width=width, length=length,
                                                 count=count,
                                                 price_output=sum, markups_type=markups_name,plug=plug,
                                                 square_meter=square_meter,
                                                 linear_meter=linear_meter)

    return low_tides_calc


def calc_flashing(flashing_id, width, length, count, markups_type):
    flashing = Flashing.objects.get(id=flashing_id)
    flashing_markup = FlashingMarkups.objects.get(flashing=flashing_id)

    price_input_low_tides = flashing.price_input

    if markups_type == 0:
        in_percent = flashing_markup.markups_diler_in_percent
        markup = flashing_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = flashing_markup.markups_retail_in_percent
        markup = flashing_markup.markups_retail
        markups_name = 'Розничная'
    elif markups_type == 2:
        in_percent = flashing_markup.markups_3_in_percent
        markup = flashing_markup.markups_3
        markups_name = 'Наценка №3'

    elif markups_type == 3:
        in_percent = flashing_markup.markups_4_in_percent
        markup = flashing_markup.markups_4
        markups_name = 'Наценка №4'

    elif markups_type == 4:
        in_percent = flashing_markup.markups_5_in_percent
        markup = flashing_markup.markups_5
        markups_name = 'Наценка №5'
    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

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
                                                linear_meter=linear_meter)

    return flahsing_calc


def calc_casing(casing_id, width, length, count, markups_type):
    casing = Casing.objects.get(id=casing_id)
    casing_markup = CasingMarkups.objects.get(casing=casing_id)

    price_input_low_tides = casing.price_input

    if markups_type == 0:
        in_percent = casing_markup.markups_diler_in_percent
        markup = casing_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = casing_markup.markups_retail_in_percent
        markup = casing_markup.markups_retail
        markups_name = 'Розничная'
    elif markups_type == 2:
        in_percent = casing_markup.markups_3_in_percent
        markup = casing_markup.markups_3
        markups_name = 'Наценка №3'
    elif markups_type == 3:
        in_percent = casing_markup.markups_4_in_percent
        markup = casing_markup.markups_4
        markups_name = 'Наценка №4'
    elif markups_type == 4:
        in_percent = casing_markup.markups_5_in_percent
        markup = casing_markup.markups_5
        markups_name = 'Наценка №5'

    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    casing_calc = SlopesOfMetalCalc.objects.create(casing_id=casing.id, width=width, length=length,
                                                   count=count,
                                                   price_output=sum, markups_type=markups_name,
                                                   square_meter=square_meter,
                                                   linear_meter=linear_meter)

    return casing_calc


def calc_visors(visors_id, width, length, count, markups_type):
    visors = Visors.objects.get(id=visors_id)
    visors_markup = VisorsMarkups.objects.get(casing=visors_id)

    price_input_low_tides = visors.price_input

    if markups_type == 0:
        in_percent = visors_markup.markups_diler_in_percent
        markup = visors_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = visors_markup.markups_retail_in_percent
        markup = visors_markup.markups_retail
        markups_name = 'Розничная'
    elif markups_type == 2:
        in_percent = visors_markup.markups_3_in_percent
        markup = visors_markup.markups_3
        markups_name = 'Наценка №3'
    elif markups_type == 3:
        in_percent = visors_markup.markups_4_in_percent
        markup = visors_markup.markups_4
        markups_name = 'Наценка №4'
    elif markups_type == 4:
        in_percent = visors_markup.markups_5_in_percent
        markup = visors_markup.markups_5
        markups_name = 'Наценка №5'
    if in_percent:
        price_low_tides = price_input_low_tides + (price_input_low_tides / 100 * markup)
    else:
        price_low_tides = price_input_low_tides + markup

    sum = price_low_tides * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    visors_calc = VisorsCalc.objects.create(visors_id=visors.id, width=width, length=length,
                                            count=count,
                                            price_output=sum, markups_type=markups_name,
                                            square_meter=square_meter,
                                            linear_meter=linear_meter)

    return visors_calc


def calc_slopes_of_metal(slopes_of_metal_id, width, length, count, markups_type):
    slopes_of_metal = SlopesOfMetal.objects.get(id=slopes_of_metal_id)
    slopes_of_metal_markup = SlopesOfMetalMarkups.objects.get(slopes_of_metal=slopes_of_metal)

    price_input = slopes_of_metal.price_input

    if markups_type == 0:
        in_percent = slopes_of_metal_markup.markups_diler_in_percent
        markup = slopes_of_metal_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = slopes_of_metal_markup.markups_retail_in_percent
        markup = slopes_of_metal_markup.markups_retail
        markups_name = 'Розничная'
    elif markups_type == 2:
        in_percent = slopes_of_metal_markup.markups_3_in_percent
        markup = slopes_of_metal_markup.markups_3
        markups_name = 'Наценка №3'
    elif markups_type == 3:
        in_percent = slopes_of_metal_markup.markups_4_in_percent
        markup = slopes_of_metal_markup.markups_4
        markups_name = 'Наценка №4'
    elif markups_type == 4:
        in_percent = slopes_of_metal_markup.markups_5_in_percent
        markup = slopes_of_metal_markup.markups_5
        markups_name = 'Наценка №5'
    if in_percent:
        price = price_input + (price_input / 100 * markup)
    else:
        price = price_input + markup

    sum = price * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    slopes_of_metal_calc = SlopesOfMetalCalc.objects.create(slopes_of_metal_id=slopes_of_metal.id, width=width,
                                                            length=length,
                                                            count=count,
                                                            price_output=sum, markups_type=markups_name,
                                                            square_meter=square_meter,
                                                            linear_meter=linear_meter)

    return slopes_of_metal_calc


def calc_internal_slope(internal_slope_id, width, length, count, markups_type):
    internal_slope = InternalSlope.objects.get(id=internal_slope_id)
    internal_slope_markup = InternalSlopeMarkups.objects.get(internal_slope=internal_slope)

    price_input = internal_slope.price_input

    if markups_type == 0:
        in_percent = internal_slope_markup.markups_diler_in_percent
        markup = internal_slope_markup.markups_diler
        markups_name = 'Диллерская'
    elif markups_type == 1:
        in_percent = internal_slope_markup.markups_retail_in_percent
        markup = internal_slope_markup.markups_retail
        markups_name = 'Розничная'
    elif markups_type == 2:
        in_percent = internal_slope_markup.markups_3_in_percent
        markup = internal_slope_markup.markups_3
        markups_name = 'Наценка №3'
    elif markups_type == 3:
        in_percent = internal_slope_markup.markups_4_in_percent
        markup = internal_slope_markup.markups_4
        markups_name = 'Наценка №4'
    elif markups_type == 4:
        in_percent = internal_slope_markup.markups_5_in_percent
        markup = internal_slope_markup.markups_5
        markups_name = 'Наценка №5'
    if in_percent:
        price = price_input + (price_input / 100 * markup)
    else:
        price = price_input + markup

    sum = price * ((width * length) / 1000000)
    square_meter = (width * length) / 1000000
    linear_meter = width / 1000

    if count > 0:
        sum = sum * count
        square_meter = square_meter * count
        linear_meter = linear_meter * count

    sum = round(sum, 2)
    square_meter = round(square_meter, 2)
    linear_meter = round(linear_meter, 2)

    internal_slop_calc = InternalSlopeCalc.objects.create(internal_slope_id=internal_slope.id, width=width, length=length,
                                                          count=count,
                                                          price_output=sum, markups_type=markups_name,
                                                          square_meter=square_meter,
                                                          linear_meter=linear_meter)

    return internal_slop_calc
