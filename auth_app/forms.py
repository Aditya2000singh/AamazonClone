from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.contrib.auth.models import User

class UserRegiserForm(forms.Form):
    email = forms.EmailField(max_length=50, validators=[EmailValidator])
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    password = forms.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16)])
    confirm_password = forms.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16)])

    def is_valid(self):
        email = self.data.get('email')
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')

        # email Validation
        try:
            get_object_or_404(User, username=email)
            self.add_error('email', 'Email Already Exists')
        except:
            pass

        # password Matching Validation
        if password != confirm_password:
            self.add_error('password', 'Password not matched. ')

        return super().is_valid()


class UserLoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=16)