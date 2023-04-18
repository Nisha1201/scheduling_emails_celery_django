from celery import shared_task
# from celery.decorators import task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
@shared_task
def send_mail_task():
    print("Mail sending.......")
    subject = 'welcome to Celery world'
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ishunish1825@gmail.com',] 
    send_mail( subject, message, email_from, recipient_list, fail_silently = False )
    return "Mail has been sent........"

@shared_task
def send_hello():
    print("HELLO")
    print('Current time is:',timezone.now())