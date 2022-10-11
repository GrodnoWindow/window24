from .models import WindowDiscount, ExchangeRates


def calc_window(profile_id, fittings_id, currency, price):
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
