from django.urls import path

from auth_app.views import (
    login_view, 
    register_view, 
    verify_email, 
    forgot_password_view, 
    reset_password_view
)

app_name = 'auth_app'

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('verify_email/<str:email>/', verify_email, name='verify-email'),
    path('forgot_password/', forgot_password_view, name='forgot-password'),
    path('reset_password/<int:uid>/<str:token>/', reset_password_view, name='reset-password'),
]
