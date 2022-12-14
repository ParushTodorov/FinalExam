from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class UserCreateForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'USERNAME'
        self.fields['email'].widget.attrs['placeholder'] = 'EMAIL'
        self.fields['password1'].widget.attrs['placeholder'] = 'PASSWORD'
        self.fields['password1'].help_text = None
        self.fields['password2'].widget.attrs['placeholder'] = 'CONFIRM PASSWORD'
        self.fields['password2'].help_text = None

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2', 'age']
        field_classes = {
            'username': auth_forms.UsernameField,
        }


class UserChangeForm(auth_forms.UserChangeForm):
    password = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'FIRST NAME'
        self.fields['last_name'].widget.attrs['placeholder'] = 'LAST NAME'
        self.fields['city'].widget.attrs['placeholder'] = 'CITY'
        self.fields['age'].widget.attrs['placeholder'] = 'AGE'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'PHONE NUMBER'

    class Meta(UserCreateForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name', 'city', 'age', 'phone_number', 'photo']


