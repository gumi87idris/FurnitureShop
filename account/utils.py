from django.core.mail import send_mail


def send_welcome_email(email):
    message = f'Dear {email}, thank you for registration on our site Furnitureshop!'
    send_mail(
        'Welcome to Furnitureshop',
        message,
        'burgerkingadmin@burger.com',
        [email],
        fail_silently=False
    )
