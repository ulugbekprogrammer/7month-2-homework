from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage

# Create your views here.
def email_send(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mamajonovibrokhimjon@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request, 'index.html')

message1 = (
    "Subject here",
    "Here is the message",
    "urakovulugbek571@gmail.com",
    ["shayxon1@gmail.com"],
)

send_mass_mail((message1), fail_silently=False)


def email_send(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['mamajonovibrokhimjon@gmail.com',]
    mail = EmailMessage(subject, message, email_from, recipient_list)
    mail.attach('t129.407.11.031.00.jpg')
    mail.send()
    form = 1
    return render(request, 'index.html', context={'form': form})