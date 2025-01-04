from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from auth_app.forms import UserRegiserForm, UserLoginForm

def login_view(request, *args, **kwargs):
    errors = None
    non_field_errors = None

    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            return redirect('auth_app:register')
        
        errors = form.errors
        non_field_errors = form.non_field_errors

    return render(request=request, template_name='auth_app/login-form.html', context={'errors': errors, 'non_field_errors': non_field_errors})


def register_view(request, *args, **kwargs):
    errors = None
    if request.method == 'POST':
        form = UserRegiserForm(request.POST or None)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User(username=cleaned_data.get('email'),
                        first_name=cleaned_data.get('firstname'),
                        last_name=cleaned_data.get('lastname'))

            user.set_password(cleaned_data.get('password'))
            user.save()
            return redirect('auth_app:login')
        errors = form.errors
    return render(request=request, template_name='auth_app/register-form.html', context={'errors': errors})
