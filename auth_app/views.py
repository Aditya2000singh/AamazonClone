from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from auth_app.forms import (UserRegiserForm,
                            UserLoginForm, 
                            VerifyEmailForm, 
                            ForgotPasswordForm,
                            ResetPasswordForm)

from auth_app.mail import send_otp_mail, send_password_reset_link_mail

def login_view(request, *args, **kwargs):
    form = UserLoginForm()
    if request.POST:
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            if not form.cleaned_data.get('account_status'):
                send_otp_mail(form.cleaned_data.get('email'))
                return redirect('auth_app:verify-email', email=form.cleaned_data.get('email'))
            return redirect('shop_app:home')

    return render(request=request, template_name='auth_app/login-form.html', context={'form': form })


def register_view(request, *args, **kwargs):
    form = UserRegiserForm()
    if request.method == 'POST':
        form = UserRegiserForm(request.POST or None)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = User(username=cleaned_data.get('email'),
                        first_name=cleaned_data.get('firstname'),
                        last_name=cleaned_data.get('lastname'))

            user.set_password(cleaned_data.get('password'))
            user.is_active = False
            user.save()
            return redirect('auth_app:login')
    return render(request=request, template_name='auth_app/register-form.html', context={'form': form})


def verify_email(request, email=None, *args, **kwargs):
    form = VerifyEmailForm()
    if request.method == 'POST':
        form = VerifyEmailForm(request.POST or None)
        if form.is_valid():
            return redirect('shop_app:home')
    return render(request=request, template_name='auth_app/verify-email.html', context={'email': email, 'form': form})


def forgot_password_view(request, *args, **kwargs):
    form = ForgotPasswordForm()
    msg = ''
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            send_password_reset_link_mail(User.objects.get(username=cleaned_data.get('email')))
            msg = "Password Reset Link Has Been Shared."
    return render(request=request, template_name='auth_app/forgot-password.html', context={'form': form, 'msg':msg})


def reset_password_view(request,uid, *args, **kwargs):
    form = ResetPasswordForm()
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST or None)
        if form.is_valid():
            user = User.objects.get(pk=uid)
            user.set_password(form.cleaned_data.get('password'))
            user.save()

            return redirect('auth_app:login')
    return render(request=request, template_name='auth_app/reset-password.html', context={'form': form})
