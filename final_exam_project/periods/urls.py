from django.urls import path, include

from final_exam_project.periods.views import rent_a_car, check_for_free_cars, create_promo_periods, \
    create_period_for_preparation, PeriodForPreparationList, PeriodForPromoList, CarsForRentListView, \
    delete_promo_periods, edit_period_for_preparation

urlpatterns = [
    path('<int:pk>/rent_a_car/', rent_a_car, name='rent_a_car'),
    path('check_for_cars/', check_for_free_cars, name='check for cars'),
    path('cars_for_rent/', CarsForRentListView.as_view(), name='cars for rent'),
    path('promo_periods/', PeriodForPromoList.as_view(), name='promo periods'),
    path('promo_periods/create/', create_promo_periods, name='create promo period'),
    path('promo_periods/<int:pk>/edit/', delete_promo_periods, name='delete promo period'),
    path('preparation_periods/', PeriodForPreparationList.as_view(), name='preparation periods'),
    path('preparation_periods/create/', create_period_for_preparation, name='create preparation period'),
    path('preparation_periods/<int:pk>/edit/', edit_period_for_preparation, name='edit preparation period'),
]
