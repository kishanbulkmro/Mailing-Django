from django.shortcuts import render

# Create your views here.
from django.core.mail import BadHeaderError, send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, HttpResponseRedirect

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    to_email = request.POST.get('to_email', '')
    html_content = request.POST.get('HTMLmessage','')
    # print(subject,message,to_email,from_email)
    if subject and message and from_email and to_email:
        try:
            msg = EmailMultiAlternatives(subject, message, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            #send_mail(subject, message, from_email, [to_email])
        except BadHeaderError:
            return render(request, 'mailapp/front.html')
    else:
        return render(request, 'mailapp/front.html')

    return render(request, 'mailapp/front.html')


