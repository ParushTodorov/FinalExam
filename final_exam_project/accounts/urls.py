from django.urls import path, include

from final_exam_project.accounts.views import profile_details, profile_edit, profile, \
    SignInView, SingOutView, UserDeleteView, UserRentedCars, CreateProfileView

urlpatterns = [
    path('', profile, name='profile'),
    path('login/', SignInView.as_view(), name='profile sign in'),
    path('logout/', SingOutView.as_view(), name='profile sign out'),
    path('create/', CreateProfileView.as_view(), name='profile create'),
    path('<int:pk>/details/', profile_details, name='profile details'),
    path('<int:pk>/edit/', profile_edit, name='profile edit'),
    path('<int:pk>/rented-cars/', UserRentedCars.as_view(), name='profile rented cars'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='profile delete'),
]
