import random
from django.conf import settings
from django.core.mail import send_mail
from auth_app.models import OTPStore
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from auth_app.utils import password_reset_token

def send_otp_mail(user_email):

    subject = 'Welcome to Our Platform'
    from_email = 'shaileshcloud596@gmail.com'
    otp = random.randint(100000, 999999)
    to = [user_email]

    # Render the HTML and plain text templates
    context = {'user_name': user_email, 'otp': otp}
    html_content = render_to_string('auth_app/email_template.html', context)
    print(html_content)
    text_content = "Hello, John Doe! Welcome to our platform."
    

    # Create the email message
    email = EmailMultiAlternatives(subject, html_content,  None, to)
    email.attach_alternative(html_content, "text/html")

    # Send the email
    email.send()
    OTPStore.objects.update_or_create(email=user_email, defaults={'otp': otp, 'is_verified': False})
    
def succesful_register(user_email, user_name):
    subject = 'Welcome to Amazon Clone!'
    from_email = 'shaileshcloud596@gmail.com'  
    to = [user_email]
    context = {
        'user_name': user_email,
    }

    # Render the HTML content using a template
    html_content = render_to_string('auth_app/welcome_email_template.html', context)

    # Create the email message
    email = EmailMultiAlternatives(
        subject=subject,
        body="Welcome to Amazon Clone!",  
        from_email=from_email,
        to=to,
    )
    email.attach_alternative(html_content, "text/html") 
    email.send()
        
    


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


