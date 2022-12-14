from django import forms
from final_exam_project.cars.models import Cars


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'


class CarEditForm(CarCreateForm):
    pass


class CarDeleteForm(CarCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _,  field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance
