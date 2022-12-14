from django.contrib import admin

from final_exam_project.cars.models import Cars


@admin.register(Cars)
class Car(admin.ModelAdmin):
    list_display = ("model", "type", "fuel", "year", "price_per_day")
    list_filter = ("model", "type", "fuel", "year", "price_per_day")
    search_fields = ("model", "type", "fuel", "year", "price_per_day")
    ordering = ("model",)

