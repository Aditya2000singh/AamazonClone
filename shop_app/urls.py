from django.urls import path 

from shop_app.views import home_view
app_name = 'shop_app'

urlpatterns = [
    path('home/', home_view, name='home'),
]
