from celery import shared_task
import time
from .views import MailSend,DetailView,subscribed_category,send_mail
from django.template.loader import render_to_string
from .models import Post
from django.core.mail import EmailMultiAlternatives

@shared_task
def post_mail_for_users(self, request, *args, **kwargs):
    post_mail = Post
    html_content = render_to_string(
        'mail_created.html', )
    msg = EmailMultiAlternatives(
        subject=f'{post_mail.title} ',
        body=post_mail.text,  # это то же, что и message
        from_email='ponialponyal@yandex.ru',
        to=['illyka@yandex.ru'],  # это то же, что и recipients_list
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html

    msg.send()  # отсылаем

