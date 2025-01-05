import random
from django.core.mail import send_mail
from auth_app.models import OTPStore

def send_otp_mail(email):
    subject = "Account active Request"
    otp = random.randint(100000, 999999)
    message = f"OPT => {otp}"
    recipient_list = ['shaileshgupta596@gmail.com']
    send_mail(subject, message, None, recipient_list)
    OTPStore.objects.update_or_create(email=email, defaults={'otp': otp, 'is_verified': False})


