from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model, login

from final_exam_project.accounts.forms import UserCreateForm, UserChangeForm
from final_exam_project.accounts.models import AppUser
from final_exam_project.periods.models import PeriodForRent

UserModel = get_user_model()


def profile(request):
    if request.user.pk:
        return redirect('profile details', pk=request.user.pk)

    return render(request, 'profile/profile-login/profile-log-or-create.html')


class CreateProfileView(views.CreateView):
    template_name = 'profile/profile-create.html'
    form_class = UserCreateForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'profile/profile-login/profile-sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SingOutView(auth_views.LogoutView):
    template_name = 'profile/profile-login/profile-log-out.html'
    success_url = reverse_lazy('index')


class UserRentedCars(views.ListView):
    template_name = 'profile/profile-rented-cars.html'
    model = PeriodForRent
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        if not self.request.user.pk == self.kwargs['pk']:
            return redirect('profile rented cars', pk=self.request.user.pk)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = PeriodForRent.objects.filter(user_id=self.kwargs['pk'])
        context['date_now'] = datetime.now().date()

        return context


@login_required
def profile_details(request, pk):
    if pk != request.user.pk:
        return redirect('profile details', pk=request.user.pk)

    user = AppUser.objects.get(pk=pk)
    context = {
        'user': user,
        'pk': pk
    }

    return render(request, 'profile/profile-details.html', context)


@login_required
def profile_edit(request, pk):
    if pk != request.user.pk:
        return redirect('profile details', pk=request.user.pk)

    user = AppUser.objects.get(pk=pk)

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()

            return redirect('profile details', pk=pk)
    else:
        user_form = UserChangeForm(instance=user)

    context = {
        'user_form': user_form,
        'pk': pk
    }
    print(context['pk'])

    return render(request, 'profile/profile-edit.html', context)


class UserDeleteView(views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
