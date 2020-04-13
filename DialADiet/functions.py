from django.core.mail import send_mail


def mail(receiver, subject, body):
    return send_mail(subject, body, 'drmanishabandishti@gmail.com', [receiver], fail_silently=False)
