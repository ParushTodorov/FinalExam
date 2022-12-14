from abc import ABC

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from final_exam_project.cars.models import Cars
from final_exam_project.cars.forms import CarCreateForm, CarDeleteForm, CarEditForm


@login_required
def car_create(request):
    if not request.user.is_staff:
        return redirect('catalogue')

    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'car/car-create.html', context)


class CarDetailView(views.DetailView):
    template_name = 'car/car-details.html'
    model = Cars


class CarEditView(views.UpdateView, LoginRequiredMixin, ABC):
    template_name = 'car/car-edit.html'
    form_class = CarEditForm
    model = Cars
    success_url = 'car details'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            return redirect('car details', pk=self.kwargs['pk'])

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        return context

    def get_success_url(self):
        return reverse_lazy('car details', kwargs={
            'pk': self.kwargs['pk'],
        })


@login_required
def car_delete(request, pk):
    car = Cars.objects.get(pk=pk)

    if not request.user.is_staff:
        return redirect('car details', pk=pk)

    if request.method == 'POST':
        form = CarDeleteForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarDeleteForm(instance=car)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'car/car-delete.html', context)
