from django.contrib import admin
from auth_app.models import OTPStore

@admin.register(OTPStore)
class OTPStoreAdminForm(admin.ModelAdmin):
    pass
