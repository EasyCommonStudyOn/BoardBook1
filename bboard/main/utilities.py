from django.conf import settings
from django.template.loader import render_to_string
from django.core.signing import Signer
from datetime import datetime
from os.path import splitext
from django.core.mail import send_mail
from django.contrib.sites.models import Site

signer = Signer()


def send_activation_notification(user):
    allowed_hosts = settings.ALLOWED_HOSTS
    host = 'http://' + allowed_hosts[0] if allowed_hosts else 'http://localhost:8000'

    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context).strip()
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)


def get_timestampt_path(instance, filename):
    return '{}{}'.format(datetime.now().timestamp(), splitext(filename)[1])


def send_new_comment_notification(comment):
    current_site = Site.objects.get_current()
    host = 'http://' + current_site.domain

    author = comment.bb.author
    context = {'author': author, 'host': host, 'comment': comment}

    subject = render_to_string('email/new_comment_letter_subject.txt', context).strip()
    body_text = render_to_string('email/new_comment_letter_body.txt', context)

    send_mail(subject, body_text, 'from@example.com', [author.email], fail_silently=False)
