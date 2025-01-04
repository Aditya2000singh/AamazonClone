from django.urls import path

from auth_app.views import (
    login_view, register_view
)

app_name = 'auth_app'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
