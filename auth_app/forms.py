from django import forms
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.contrib.auth.models import User

from auth_app.validators import is_email_present

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
    email = forms.EmailField(max_length=50, validators=[EmailValidator, is_email_present])
    password = forms.CharField(max_length=16, validators=[MinLengthValidator(8), MaxLengthValidator(16)])


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('Email & Password Doesnot Matched.')
        
        return cleaned_data
        