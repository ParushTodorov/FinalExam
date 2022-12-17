from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic as views

from final_exam_project.cars.models import Cars
from final_exam_project.periods.calculations import check_is_car_free, calculate_price, cars_for_visualisations
from final_exam_project.periods.forms import RentPeriodCreateForm, CheckForFreeCarsInPeriodForm, PeriodForPromoForm, \
    PeriodForPreparationForm, PeriodForPromoDeleteForm, PeriodForPreparationChangeForm
from final_exam_project.periods.models import PeriodForRent, PeriodForPreparation, PeriodForPromo


def check_for_free_cars(request):
    if request.method == 'POST':
        form = CheckForFreeCarsInPeriodForm(request.POST, request.FILES)
        if form.is_valid():
            cars = cars_for_visualisations(
                form.cleaned_data['start_date'],
                form.cleaned_data['end_date'],
                form.cleaned_data['province'])

            context = {
                'object_list': cars,
            }

            print(request)

            return render(request, 'periods/catalogue-cars-for-rent.html', context)
    else:
        form = CheckForFreeCarsInPeriodForm()

    context = {
        'form': form,
    }

    return render(request, 'periods/check_for_period.html', context)


class CarsForRentListView(views.ListView):
    model = Cars
    template_name = 'periods/catalogue-cars-for-rent.html'
    paginate_by = 3


@login_required
def rent_a_car(request, pk):
    initial_data = {
        'user': request.user,
        'car': pk,
        'total_price': 1
    }

    car = Cars.objects.get(pk=pk)

    if request.method == 'POST':
        form = RentPeriodCreateForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect('profile details', pk=request.user.id)
    else:
        form = RentPeriodCreateForm(initial=initial_data)
        print(form.initial)

    context = {
        'form': form,
        'pk': pk,
        'car': car
    }

    return render(request, 'periods/period_create.html', context)


@login_required
def create_promo_periods(request):
    if not request.user.is_staff:
        return redirect('index')

    if request.method == 'POST':
        form = PeriodForPromoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('promo periods')
    else:
        form = PeriodForPromoForm()

    context = {
        'form': form,
    }

    return render(request, 'periods/../../templates/periods-admin/period-for-promo-create.html', context)


@login_required
def delete_promo_periods(request, pk):
    if not request.user.is_staff:
        return redirect('index')

    period = PeriodForPromo.objects.get(pk=pk)

    if request.method == 'POST':
        form = PeriodForPromoDeleteForm(request.POST, request.FILES, instance=period)
        if form.is_valid():
            form.save()

            return redirect('promo periods')
    else:
        form = PeriodForPromoDeleteForm(instance=period)

    context = {
        'form': form,
        'pk': pk
    }

    return render(request, 'periods/../../templates/periods-admin/period-for-promo-delete.html', context)


@login_required
def create_period_for_preparation(request):
    if not request.user.is_staff:
        return redirect('catalogue')

    if request.method == 'POST':
        form = PeriodForPreparationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('preparation periods')
    else:
        form = PeriodForPreparationForm()

    context = {
        'form': form,
    }

    return render(request, 'periods/../../templates/periods-admin/period-for-preparation-create.html', context)


@login_required
def edit_period_for_preparation(request, pk):
    if not request.user.is_staff:
        return redirect('catalogue')

    period = PeriodForPreparation.objects.get(pk=pk)

    if request.method == 'POST':
        form = PeriodForPreparationChangeForm(request.POST, request.FILES, instance=period)
        if form.is_valid():
            form.save()

            return redirect('preparation periods')
    else:
        form = PeriodForPreparationChangeForm(instance=period)

    context = {
        'form': form,
        'period': period
    }

    return render(request, 'periods/../../templates/periods-admin/period-for-preparation-edit.html', context)


class PeriodForPromoList(views.ListView):
    template_name = 'periods/../../templates/periods-admin/period-for-promo-list.html'
    model = PeriodForPromo
    paginate_by = 10
    ordering = ['start_date']

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('index')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['date_now'] = datetime.now().date()
        return context


class PeriodForPreparationList(views.ListView):
    template_name = 'periods/../../templates/periods-admin/period-for-preparation-list.html'
    model = PeriodForPreparation

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('index')

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['length'] = len(PeriodForPreparation.PROVINCE_CHOICES)
        return context
