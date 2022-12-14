from django.contrib import admin

from final_exam_project.periods.forms import RentPeriodCreateForm, PeriodForPromoForm, PeriodForPreparationForm
from final_exam_project.periods.models import PeriodForRent, PeriodForPromo, PeriodForPreparation


@admin.register(PeriodForRent)
class PeriodForRent(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "user", "car", "city", "total_price")
    list_filter = ("start_date", "end_date", "user", "car", "city", "total_price")
    search_fields = ("start_date", "end_date", "user", "car", "city", "total_price")
    ordering = ("start_date", "user", "car", "city", "total_price")
    add_form = RentPeriodCreateForm


@admin.register(PeriodForPromo)
class PeriodForPromo(admin.ModelAdmin):
    list_display = ("start_date", "end_date", "discount")
    list_filter = ("start_date", "end_date", "discount")
    search_fields = ("start_date", "end_date", "discount")
    ordering = ("start_date", "end_date", "discount")


@admin.register(PeriodForPreparation)
class PeriodForPreparation(admin.ModelAdmin):
    list_display = ("province", "days_for_preparation")
    list_filter = ("province", "days_for_preparation")
    search_fields = ("province", "days_for_preparation")
    ordering = ("province", "days_for_preparation")
    add_form = PeriodForPreparationForm
