from datetime import datetime

from django.views import generic as views
from django.shortcuts import render, redirect
from final_exam_project.cars.models import Cars
from final_exam_project.periods.models import PeriodForPromo


def index(request):
    promo = PeriodForPromo.objects\
        .filter(start_date__gte=datetime.now().date())\
        .filter(end_date__lte=datetime.now().date())

    if not promo:
        return render(request, 'core/index.html')

    context = {
        'promo': promo[0]
    }

    return render(request, 'core/index.html', context)


class CatalogueListView(views.ListView):
    model = Cars
    template_name = 'core/catalogue.html'
    paginate_by = 3


def administration_panel(request):
    if not request.user.is_staff:
        return redirect('index')
    return render(request, 'core/administration_panel.html')



