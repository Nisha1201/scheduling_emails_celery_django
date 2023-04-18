from django.shortcuts import render
from django.http import HttpResponse
from .task import *
# from .helper import *

def index(request):
    # send_mail_without_celery()
    # print(send_mail_without_celery(),"ssssssssssssssseeeeeeennndddddddd")
    send_mail_task.delay()
    print(send_mail_task.delay(),'*******************')

    send_hello.delay() 
    
    # sleepy.delay(5)
    # print(add(3,4))
    # result = add.delay(3, 5)
  
    # return HttpResponse("<h1>Hello ,from send without celery show</h1>")
    return HttpResponse("<h1>Hello ,from send mail show</h1>")



# commands which are using during the running:
# python3 manage.py runserver
# celery -A scheduling_emails_with_celery_django  worker --pool=solo -l info
# celery -A scheduling_emails_with_celeryjango beat -l INFO