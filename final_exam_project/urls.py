from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from final_exam_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('final_exam_project.common.urls')),
    path('profile/', include('final_exam_project.accounts.urls')),
    path('cars/', include('final_exam_project.cars.urls')),
    path('periods/', include('final_exam_project.periods.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
