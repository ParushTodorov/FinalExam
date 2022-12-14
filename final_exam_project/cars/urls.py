from django.urls import path, include

from final_exam_project.cars.views import car_create, car_delete, CarDetailView, CarEditView

urlpatterns = [
    path('create/', car_create, name='car create'),
    path('<int:pk>/details/', CarDetailView.as_view(), name='car details'),
    path('<int:pk>/edit/', CarEditView.as_view(), name='car edit'),
    path('<int:pk>/delete/', car_delete, name='car delete'),
]
