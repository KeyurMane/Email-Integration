from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

def sendmailview(request):
    subject = 'welcome to Django'
    message = f'Hi thank you for using djago email integration.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['keyurmane196@gmail.com', ]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse('mail sent')

