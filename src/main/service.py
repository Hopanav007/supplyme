from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Вы пытаетесь заригистрироваться на SupplyMe',
        'Если это действительно вы введите на странице код снизу:',
        [user_email],
        fail_silently=False,
    )