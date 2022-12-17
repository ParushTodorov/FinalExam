import datetime

from django import forms
from django.core.exceptions import ValidationError

from final_exam_project import settings
from final_exam_project.periods.calculations import check_is_car_free, check_is_promo_period, calculate_price
from final_exam_project.periods.models import PeriodForRent, PeriodForPromo, PeriodForPreparation


class CheckForFreeCarsInPeriodForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
    )

    end_date = forms.DateField(
        input_formats=settings.DATE_INPUT_FORMATS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['end_date'].widget.attrs['placeholder'] = 'YYYY-MM-DD'

    class Meta:
        model = PeriodForRent
        fields = ['start_date', 'end_date', 'province']

    def clean(self):
        cleaned_data = self.cleaned_data
        self.validate_unique()
        if not self.is_valid():
            return

        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        if self.cleaned_data['start_date'] < datetime.date.today():
            raise ValidationError('The date cannot be in the past!')

        if start_date > end_date:
            raise ValidationError('Start date must be before end date!')

        return cleaned_data


class RentPeriodCreateForm(CheckForFreeCarsInPeriodForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['placeholder'] = 'CITY'
        self.fields['address'].widget.attrs['placeholder'] = 'ADDRESS'
        self.fields['comment'].widget.attrs['placeholder'] = 'MORE INFO'

    class Meta:
        model = PeriodForRent
        fields = ['start_date', 'end_date', 'province', 'city', 'address', 'comment', 'car', 'user', 'total_price']

        widgets = {
            'user': forms.HiddenInput(),
            'car': forms.HiddenInput(),
            'total_price': forms.HiddenInput(),
        }

    def clean(self):
        super().clean()

        if not check_is_car_free(
                self.cleaned_data['start_date'],
                self.cleaned_data['end_date'],
                self.cleaned_data['province'],
                self.cleaned_data['car']
        ):
            raise ValidationError(f'{self.cleaned_data["car"].model} is rented for period '
                                  f'from {self.cleaned_data["start_date"]} to {self.cleaned_data["end_date"]}')

        total_price = calculate_price(
            self.cleaned_data['start_date'],
            self.cleaned_data['end_date'],
            self.cleaned_data['car']
        )

        self.cleaned_data['total_price'] = total_price


class PeriodForPromoForm(CheckForFreeCarsInPeriodForm):
    class Meta:
        model = PeriodForPromo
        fields = ['start_date', 'end_date', 'discount']

    def clean(self):
        super().clean()

        if not check_is_promo_period(self.cleaned_data['start_date'],
                                     self.cleaned_data['end_date']):
            raise ValidationError(f'There is other promotion in period '
                                  f'between {self.cleaned_data["start_date"]} and {self.cleaned_data["end_date"]}')


class PeriodForPromoDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _,  field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = PeriodForPromo
        fields = ['start_date', 'end_date', 'discount']

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance


class PeriodForPreparationForm(forms.ModelForm):

    class Meta:
        model = PeriodForPreparation
        fields = '__all__'


class PeriodForPreparationChangeForm(PeriodForPreparationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = PeriodForPreparation
        fields = '__all__'
        widgets = {
            'province': forms.HiddenInput(),
        }
