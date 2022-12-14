import datetime

from final_exam_project.cars.models import Cars
from final_exam_project.periods.models import PeriodForRent, PeriodForPromo, PeriodForPreparation


def cars_for_visualisations(sd, ed, province):
    cars = []

    cars_all = Cars.objects.all()

    for car in cars_all:
        if not check_is_car_free(sd, ed, province, car):
            continue

        cars.append(car)

    return cars


def check_is_car_free(start_date, end_date, province, car):
    preparation_period = PeriodForPreparation.objects.filter(province=province)

    days = 1

    if preparation_period[0]:
        days = preparation_period[0].days_for_preparation

    start_date -= datetime.timedelta(days)

    if not PeriodForRent.objects.filter(car_id=car.pk)\
            .filter(start_date__gte=start_date)\
            .filter(start_date__lte=end_date) \
            or not PeriodForRent.objects.filter(car_id=car.pk)\
            .filter(end_date__gte=start_date)\
            .filter(end_date__lte=end_date):
        return True

    return False


def calculate_price(sd, ed, car):
    price = 0
    days = (datetime.date(ed.year, ed.month, ed.day) - datetime.date(sd.year, sd.month, sd.day)).days + 1

    promo_periods = PeriodForPromo.objects\
        .filter(start_date__lte=ed) \
        .filter(end_date__gte=sd)\

    if not promo_periods:
        price = ((datetime.date(ed.year, ed.month, ed.day) - datetime.date(sd.year, sd.month, sd.day)).days + 1) * \
                car.price_per_day

        return price

    for x in range(days):
        date = sd + datetime.timedelta(x)
        discount = 0

        for period in promo_periods:
            if period.start_date <= date <= period.end_date:
                discount = period.discount
                break

        price += car.price_per_day * (100 - discount) / 100

    return price


def check_is_promo_period(start_date, end_date):
    if not PeriodForPromo.objects\
            .filter(start_date__gte=start_date)\
            .filter(start_date__lte=end_date) \
            or not PeriodForPromo.objects\
            .filter(end_date__gte=start_date)\
            .filter(end_date__lte=end_date):
        return True

    return False
