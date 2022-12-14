from django.urls import path

from final_exam_project.common.views import index, CatalogueListView, administration_panel

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', CatalogueListView.as_view(), name='catalogue'),
    path('administration/', administration_panel, name='administration'),
]
