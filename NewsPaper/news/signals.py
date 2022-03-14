from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Post

"""@receiver(post_save, sender=Post)
def save_post(created, **kwargs):
    post_turn = kwargs['instance']
    subscribers_list = {user.email
                        for category in post_turn.Category.all()
                        for user in category.subscribers.all()}
    email_from = settings.DEFAULT_FROM_EMAIL

    if created:
        subject = 'В вашей любимой категории новая статья!'
        text_message = f'В вашей любимой категории новая статья:'
    else:
        subject = 'В категориях, на которые вы подписаны, была изменена статья'
        text_message = f'В категориях, на которые вы подписаны,была изменена статья:'
    html_template = render_to_string('post_create.html', {'post': post_turn, 'subject': subject})

    msg = EmailMultiAlternatives(subject, text_message, email_from, list(subscribers_list))
    msg.attach_alternative(html_template, 'text/html')
    msg.send()"""