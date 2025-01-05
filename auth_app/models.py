from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator
# Create your models here.

class OTPStore(models.Model):
    email = models.EmailField(max_length=50, validators=[EmailValidator])
    otp = models.CharField(max_length=6, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    is_verified = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.email} => {self.otp}"
