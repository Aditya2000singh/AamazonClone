from django.urls import path

from auth_app.views import (
    login_view, register_view, verify_email
)

app_name = 'auth_app'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('verify_email/<str:email>/', verify_email, name='verify-email'),
]
