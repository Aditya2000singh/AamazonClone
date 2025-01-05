import random
from django.conf import settings
from django.core.mail import send_mail
from auth_app.models import OTPStore

from auth_app.utils import password_reset_token

def send_otp_mail(email):
    subject = "Account active Request"
    otp = random.randint(100000, 999999)
    message = f"OPT => {otp}"
    recipient_list = ['shaileshgupta596@gmail.com']
    send_mail(subject, message, None, recipient_list)
    OTPStore.objects.update_or_create(email=email, defaults={'otp': otp, 'is_verified': False})


def send_password_reset_link_mail(user):
    token = password_reset_token.make_token(user)
    uid = user.pk
    reset_link = f"http://127.0.0.1:8000/reset_password/{uid}/{token}/"
    send_mail(
        subject="Password Reset Request",
        message=f"Click the link to reset your password: {reset_link}",
        from_email=None,
        recipient_list=[user.username],
    )


